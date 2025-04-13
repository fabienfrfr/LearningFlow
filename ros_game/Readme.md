###### Attribution required : Fabien Furfaro (CC 4.0 BY NC ND SA)

---

# Astuce

Utilisation de plusieurs onglets de Terminal : Maj+Ctrl+T

Sublime text : 

	- Glisser le dossier pour avoir l'arborescence
	- Installer des modules/packages via Ctrl+Maj+p
	- Package "Terminus" et éditer Key-Binding : Alt+1 (tips : ipython3) --> pour testing

# ROS installation

Sous Linux (Ubuntu) :

``` 
sudo apt install ros-desktop-full
sudo apt install libhwloc-contrib-plugins proj-bin mpi-default-bin vtk9-doc vtk9-examples
#sudo apt install gazebo
# test result (catkin_make)
sudo apt install libgtest-dev libgmock-dev python3-nose
```

ROS basique est inclus dans Debian (https://wiki.debian.org/DebianScience/Robotics/ROS/Packages), mais le reste est à builder à la main (https://answers.ros.org/question/399664/will-ros-noetic-support-ubuntu-2204/). Néanmoins, ROS1 ne sera pas supporté sur 22.04, il sera préférable de faire un portage vers ROS2 ensuite.

# Create a project

```
mkdir -p ProjectName/src
cd ProjectName/
catkin_make
```

# Create ros package

```
cd src/
catkin_create_pkg pkg_name dependency1 dependency2 # (...) dependency is python module
```

Dans pkg_name, le fichier package.xml contient les informations pour le build.

En python, on utilise principalement les dépendances "rospy" et "std_msgs".


# Create Nodes

Pour lancer les nodes "rosrun", il est nécessaire que "roscore" soit exécuté dans une fenêtre.

Le roscore est le cœur "master" du middleware ROS. Un nœud est un fichier et les topics sont un moyen de communiquer avec les nœuds.

Les nœuds sont contenus dans les packages et en Python, c'est un fichier avec l'extension ".py". Pour cela, on crée un dossier "scripts" dans le package qui contiendra les différents nœuds python.

Il faut ensuite préciser les nœuds dans le CMakeLists.txt :
```
catkin_install_python(PROGRAMS script/node1.py script/node2.py ... )
```

Aller dans le dossier parent et lancer la commande "catkin_make" pour recompiler. À partir d'ici, le script peut être modifié sans avoir besoin de recompiler (pour python). Pour lancer le node :

```
# terminal 1
roscore
# terminal 2
source devel/setup.bash
rosrun tutorial publisher_node.py
# terminal 3
source devel/setup.bash
rosrun tutorial subscriber_node.py
```

Remarque : La source doit toujours être lancée pour que rosrun fonctionne. Si on arrête le rosrun publisher, le subscriber est en attente.

Pour voir les topics en cours et les messages :

```
rostopic list
rostopic echo /talking_topic
```

# Create Message

Un message est un moyen d'utiliser des topics pré-paramétré. Pour cela on crée un dossier "msg" contenant un fichier "MSG.msg" avec des variables (string, float, etc.). Dans le code, on importe le fichier msg comme un module python (from import).

Pour utiliser des messages, il faut le préciser dans le fichier "package.xml" en dé-commentant les lignes :

```
  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
```

Ensuite, dans le CMakeList, on precise :

```
add_message_files(
   FILES
   MSG.msg
    )

generate_messages(
   DEPENDENCIES
   std_msgs
 )
```

# Create Service

Lorsqu'on veut utiliser une communication synchrone bidirectionnelle entre plusieurs nœuds (client/serveur), il est plus intéressant d'utiliser des services. Pour cela, on crée un dossier "srv" contenant des fichiers "multiplier.srv". Ces fichiers contiennent les informations d’entrée et de sortie séparée par "---". Tout comme les messages, les services sont importés comme des modules en python.

Ensuite, dans le CMakeList, on précise :

```
add_service_files(
   FILES
   multiplier.srv
 )
```

Pour voir les services en cours :

```
rosservice list
rosservice info /multiplier
```

Pour call un service sur la console :

```
rosservice call /multiplier "{a:10 , b:7}" # attention python2 != python3
```

# Create Launch File

Pour lancer plusieurs nodes en même temps suivant une certaine logique, on utilise des launchfiles. Pour cela, on créer un dossier "launch" dans le package, il contiendra les fichiers ".launch". Le langage ressemble à du HTML.

```
<launch>
   <node pkg="tutorial" type="service_server_node.py" name="service_serveur_node" output="screen"> </node>
   <node pkg="tutorial" type="service_client_node.py" name="service_client_node" output="screen"> </node>
</launch>
```

Pour que cela marche, il faut que les fichiers ".py" soit defini comme executable :

```
ls -la
chmod +x service_server_node.py
chmod +x service_client_node.py

```

Une fois fait, il suffit de lancer la commande :

```
source devel/setup.bash
roslaunch tutorial ros_service_example.launch

```

Le core ros est aussi lancé en même temps, pas besoin de le lancer.

# Objectif


Utilisation de python et ROS + websocket GODOT + Flask

