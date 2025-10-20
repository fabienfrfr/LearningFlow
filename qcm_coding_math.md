# **Checklist des Thématiques Couvertes**

## **Python**
- [x] Syntaxe et erreurs courantes
- [x] Algorithmes simples
- [x] Structures de données
- [x] Fonctions et portée des variables
- [x] Compréhensions de listes et générateurs
- [x] Exceptions et gestion d’erreurs
- [x] POO (classes, héritage, surcharge)
- [x] Manipulation de fichiers
- [x] Défis d’algorithmie (nombre manquant, paires, etc.)
- [x] Modules et bibliothèques standards

## **Django/SQL**
- [x] Structure du projet Django
- [x] Cycle requête-réponse
- [x] Modèles et ORM
- [x] Requêtes ORM et SQL
- [x] Liens entre modèles (ForeignKey, ManyToMany, etc.)
- [x] Formulaires et validations
- [x] Templates et filtres
- [x] Sécurité et sessions
- [x] Django REST Framework
- [x] SQL pratique
- [x] Optimisation et déploiement

## **ML/IA**
| Thématique                     | Couvert |
|--------------------------------|---------|
| Python pour la Data Science    | ✅      |
| Machine Learning (ML)          | ✅      |
| Deep Learning                   | ✅      |
| NLP (Natural Language Processing)| ✅      |
| Computer Vision                | ✅      |
| MLOps                          | ✅      |
| Big Data & Outils (Spark, Dask) | ✅      |
| Statistiques & Mathématiques   | ✅      |



# **40+ Questions/Réponses Python**

---

## **1. Syntaxe et Erreurs Courantes**
### **Q1** : Corrige l’erreur : `if x = 5: print("x est 5")`
**Réponse** :
```python
if x == 5: print("x est 5")
```

### **Q2** : Pourquoi `print("Hello, World"` génère une erreur ?
**Réponse** : Il manque un guillemet fermant : `print("Hello, World")`.

### **Q3** : Corrige l’indentation : `for i in range(5):print(i)`
**Réponse** :
```python
for i in range(5):
    print(i)
```

### **Q4** : Pourquoi `x = [1, 2, 3]; x[3] = 4` génère une erreur ?
**Réponse** : L’index `3` est hors limites (la liste a une longueur de 3).

### **Q5** : Corrige ce code (piège des listes par défaut) :
```python
def foo(a, b=[]):
    b.append(a)
    return b
```
**Réponse** :
```python
def foo(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b
```

---

## **2. Algorithmes Simples**
### **Q6** : Inverser une chaîne de caractères.
**Réponse** :
```python
def reverse_string(s):
    return s[::-1]
```

### **Q7** : Vérifier si une chaîne est un palindrome.
**Réponse** :
```python
def is_palindrome(s):
    return s == s[::-1]
```

### **Q8** : Compter les occurrences d’un caractère dans une chaîne.
**Réponse** :
```python
def count_char(s, c):
    return s.count(c)
```

### **Q9** : Trier une liste d’entiers sans utiliser `sort()`.
**Réponse** :
```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
```

### **Q10** : Trouver le plus grand nombre dans une liste.
**Réponse** :
```python
def max_number(lst):
    return max(lst)
```

---

## **3. Structures de Données**
### **Q11** : Différence entre une liste et un tuple.
**Réponse** : Les listes sont mutables, les tuples sont immuables.

### **Q12** : Fusionner deux dictionnaires en Python 3.9+.
**Réponse** :
```python
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2
```

### **Q13** : Supprimer les doublons d’une liste tout en conservant l’ordre.
**Réponse** :
```python
lst = [1, 2, 2, 3]
unique = list(dict.fromkeys(lst))
```

### **Q14** : Différence entre `set` et `frozenset`.
**Réponse** : `set` est mutable, `frozenset` est immuable.

### **Q15** : Accéder à la dernière valeur d’un tuple.
**Réponse** :
```python
t = (1, 2, 3)
last = t[-1]
```

---

## **4. Fonctions et Portée des Variables**
### **Q16** : Que fait ce code ?
```python
def foo(a, *args):
    return a + sum(args)
```
**Réponse** : Retourne la somme de `a` et de tous les arguments supplémentaires.

### **Q17** : Différence entre `*args` et `**kwargs`.
**Réponse** : `*args` pour les arguments positionnels, `**kwargs` pour les arguments nommés.

### **Q18** : Pourquoi ce code génère une erreur ?
```python
x = 10
def foo():
    print(x)
    x = 5
foo()
```
**Réponse** : `x` est référencé avant d’être défini dans la portée locale.

### **Q19** : Écris une fonction récursive pour calculer la factorielle.
**Réponse** :
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
```

### **Q20** : Que fait `lambda x: x**2` ?
**Réponse** : Crée une fonction anonyme qui retourne le carré de `x`.

---

## **5. Compréhensions de Listes et Générateurs**
### **Q21** : Réécris cette boucle avec une compréhension de liste :
```python
result = []
for i in range(10):
    result.append(i**2)
```
**Réponse** :
```python
result = [i**2 for i in range(10)]
```

### **Q22** : Extraire les nombres pairs d’une liste.
**Réponse** :
```python
pairs = [x for x in lst if x % 2 == 0]
```

### **Q23** : Différence entre une liste et un générateur.
**Réponse** : Les listes stockent tous les éléments en mémoire, les générateurs produisent les éléments à la volée.

### **Q24** : Écris un générateur pour les nombres de Fibonacci.
**Réponse** :
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### **Q25** : Utilisation de `yield` dans une fonction.
**Réponse** :
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

---

## **6. Exceptions et Gestion d’Erreurs**
### **Q26** : Corrige ce bloc `try/except` :
```python
try:
    x = 1/0
except:
    print("Erreur")
```
**Réponse** :
```python
try:
    x = 1/0
except ZeroDivisionError:
    print("Erreur")
```

### **Q27** : Lever une exception personnalisée.
**Réponse** :
```python
raise ValueError("Message d'erreur personnalisé")
```

### **Q28** : Différence entre `except Exception` et `except`.
**Réponse** : `except Exception` attrape toutes les exceptions sauf `SystemExit` et `KeyboardInterrupt` ; `except` attrape tout (déconseillé).

### **Q29** : Écris un bloc `try/except/else/finally`.
**Réponse** :
```python
try:
    x = 1/1
except ZeroDivisionError:
    print("Division par zéro")
else:
    print("Pas d'erreur")
finally:
    print("Toujours exécuté")
```

### **Q30** : Ignorer une exception spécifique.
**Réponse** :
```python
try:
    x = 1/0
except ZeroDivisionError:
    pass
```

---

## **7. POO (Programmation Orientée Objet)**
### **Q31** : Écris une classe `Personne` avec une propriété `nom_complet`.
**Réponse** :
```python
class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"
```

### **Q32** : Écris une classe `CompteBancaire` avec des méthodes `deposer` et `retirer`.
**Réponse** :
```python
class CompteBancaire:
    def __init__(self, solde=0):
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
```

### **Q33** : Surcharge d’opérateurs (`__add__`).
**Réponse** :
```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)
```

### **Q34** : Utilisation de `@classmethod` et `@staticmethod`.
**Réponse** :
```python
class MaClasse:
    @classmethod
    def methode_classe(cls):
        pass
    @staticmethod
    def methode_statique():
        pass
```

### **Q35** : Héritage multiple et MRO.
**Réponse** :
```python
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
```

---

## **8. Manipulation de Fichiers**
### **Q36** : Lire un fichier et retourner la ligne la plus longue.
**Réponse** :
```python
def longest_line(filename):
    with open(filename) as f:
        return max(f.readlines(), key=len)
```

### **Q37** : Écrire dans un fichier avec un timestamp.
**Réponse** :
```python
from datetime import datetime
with open("log.txt", "a") as f:
    f.write(f"{datetime.now()}: Nouvelle entrée\n")
```

---

## **9. Défis d’Algorithmie**
### **Q38** : Trouver le nombre manquant dans une liste de 1 à n.
**Réponse** :
```python
def missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)
```

### **Q39** : Former le plus grand nombre possible à partir d’une liste d’entiers.
**Réponse** :
```python
from functools import cmp_to_key
def largest_number(lst):
    def compare(a, b):
        return -1 if str(a) + str(b) > str(b) + str(a) else 1
    lst = sorted(lst, key=cmp_to_key(compare))
    return ''.join(map(str, lst))
```

### **Q40** : Trouver toutes les paires qui donnent une somme cible.
**Réponse** :
```python
def find_pairs(lst, target):
    seen = set()
    pairs = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append([complement, num])
        seen.add(num)
    return pairs
```

---

# **40+ Questions/Réponses Django/SQL**

---

## **1. Structure du Projet Django**
### **Q1** : Fichier de configuration d’un projet Django.
**Réponse** : `settings.py`.

### **Q2** : Fichier définissant les routes principales.
**Réponse** : `urls.py` (au niveau du projet).

### **Q3** : Créer une nouvelle application.
**Réponse** :
```bash
python manage.py startapp nom_application
```

### **Q4** : Fichier contenant les modèles de données.
**Réponse** : `models.py`.

### **Q5** : Activer le mode debug.
**Réponse** : Dans `settings.py`, `DEBUG = True`.

---

## **2. Cycle Requête-Réponse**
### **Q6** : Comment Django résout-il une URL ?
**Réponse** : Via le routeur (`urls.py`), qui appelle la vue correspondante.

### **Q7** : Décorateur pour protéger contre les attaques CSRF.
**Réponse** : `@csrf_protect` ou `{% csrf_token %}` dans les formulaires.

### **Q8** : Rediriger vers une autre URL.
**Réponse** :
```python
from django.shortcuts import redirect
return redirect('/nouvelle-url/')
```

### **Q9** : Retourner une réponse JSON.
**Réponse** :
```python
from django.http import JsonResponse
return JsonResponse({"clé": "valeur"})
```

### **Q10** : Gérer une requête POST.
**Réponse** :
```python
def ma_vue(request):
    if request.method == 'POST':
        # Traiter les données POST
        pass
```

---

## **3. Modèles et ORM**
### **Q11** : Écris un modèle `Livre`.
**Réponse** :
```python
from django.db import models
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
```

### **Q12** : Créer une migration.
**Réponse** :
```bash
python manage.py makemigrations
```

### **Q13** : Appliquer une migration.
**Réponse** :
```bash
python manage.py migrate
```

### **Q14** : Filtrer les livres publiés après 2020.
**Réponse** :
```python
Livre.objects.filter(date_publication__gt="2020-01-01")
```

### **Q15** : Trier les livres par titre.
**Réponse** :
```python
Livre.objects.order_by('titre')
```

---

## **4. Requêtes ORM et SQL**
### **Q16** : Compter le nombre de livres par auteur.
**Réponse** :
```python
from django.db.models import Count
Livre.objects.values('auteur').annotate(nb_livres=Count('id'))
```

### **Q17** : Requête ORM pour `SELECT * FROM livre WHERE auteur = 'Victor Hugo'`.
**Réponse** :
```python
Livre.objects.filter(auteur='Victor Hugo')
```

### **Q18** : Utilisation de `select_related`.
**Réponse** :
```python
Livre.objects.select_related('auteur').all()
```

### **Q19** : Utilisation de `annotate`.
**Réponse** :
```python
from django.db.models import F
Livre.objects.annotate(prix_ttc=F('prix_ht') * 1.2)
```

### **Q20** : Trouver le livre le plus récent.
**Réponse** :
```python
Livre.objects.latest('date_publication')
```

---

## **5. Liens entre Modèles**
### **Q21** : Différence entre `ForeignKey` et `OneToOneField`.
**Réponse** : `ForeignKey` = relation 1:N, `OneToOneField` = relation 1:1.

### **Q22** : Relation ManyToMany entre `Livre` et `Auteur`.
**Réponse** :
```python
class Livre(models.Model):
    auteurs = models.ManyToManyField('Auteur')
```

### **Q23** : Accéder aux livres d’un auteur.
**Réponse** :
```python
auteur = Auteur.objects.get(nom='Victor Hugo')
livres = auteur.livre_set.all()
```

### **Q24** : Supprimer un auteur et ses livres.
**Réponse** :
```python
auteur.delete()  # Si `on_delete=models.CASCADE`
```

### **Q25** : Utilisation de `prefetch_related`.
**Réponse** :
```python
Livre.objects.prefetch_related('auteurs').all()
```

---

## **6. Formulaires et Validations**
### **Q26** : Créer un formulaire pour `Livre`.
**Réponse** :
```python
from django import forms
from .models import Livre
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication']
```

### **Q27** : Valider qu’un champ est unique.
**Réponse** :
```python
class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre']
        unique_together = ['titre']
```

### **Q28** : Afficher les erreurs de validation.
**Réponse** :
```html
<form>
    {{ form.non_field_errors }}
    {% for field in form %}
        {{ field.errors }}
        {{ field }}
    {% endfor %}
</form>
```

### **Q29** : Personnaliser l’affichage d’un champ.
**Réponse** :
```python
class LivreForm(forms.ModelForm):
    titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'mon-style'}))
```

### **Q30** : Utiliser un formulaire pour créer un `Livre`.
**Réponse** :
```python
def create_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LivreForm()
    return render(request, 'template.html', {'form': form})
```

---

## **7. Templates**
### **Q31** : Afficher une liste d’articles dans un template.
**Réponse** :
```html
{% for article in articles %}
    <h2>{{ article.titre }}</h2>
{% endfor %}
```

### **Q32** : Utilisation de filtres personnalisés.
**Réponse** :
```python
# templatetags/custom_filters.py
from django import template
register = template.Library()
@register.filter
def format_date(value):
    return value.strftime("%d/%m/%Y")
```
```html
{% load custom_filters %}
{{ livre.date_publication|format_date }}
```

---

## **8. Sécurité et Sessions**
### **Q33** : Protéger une vue contre les attaques CSRF.
**Réponse** : Utiliser `@csrf_protect` ou `{% csrf_token %}`.

### **Q34** : Gérer les sessions.
**Réponse** :
```python
request.session['clef'] = 'valeur'
```

---

## **9. Django REST Framework**
### **Q35** : Créer un `Serializer` pour `Livre`.
**Réponse** :
```python
from rest_framework import serializers
from .models import Livre
class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication']
```

### **Q36** : Créer une `ViewSet` pour `Livre`.
**Réponse** :
```python
from rest_framework import viewsets
from .models import Livre
from .serializers import LivreSerializer
class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
```

---

## **10. SQL Pratique**
### **Q37** : Requête SQL pour compter les livres par auteur.
**Réponse** :
```sql
SELECT auteur, COUNT(*) FROM livre GROUP BY auteur;
```

### **Q38** : Requête ORM équivalente à une jointure SQL.
**Réponse** :
```python
Livre.objects.select_related('auteur').filter(auteur__nom='Victor Hugo')
```

---

## **11. Optimisation et Déploiement**
### **Q39** : Éviter les requêtes N+1.
**Réponse** :
```python
livres = Livre.objects.select_related('auteur').all()
```

### **Q40** : Configurer Django avec des variables d’environnement.
**Réponse** :
```python
# settings.py
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

---

# **40 Questions/Réponses pour Data Science, IA & Machine Learning Engineer**

---

## **1. Python pour la Data Science**
### **Q1** : Comment lire un fichier CSV avec `pandas` ?
**Réponse** :
```python
import pandas as pd
df = pd.read_csv("fichier.csv")
```

### **Q2** : Comment gérer les valeurs manquantes dans un DataFrame ?
**Réponse** :
```python
df.fillna(0)  # Remplacer par 0
df.dropna()   # Supprimer les lignes avec des NaN
```

### **Q3** : Comment normaliser une colonne avec `sklearn` ?
**Réponse** :
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['colonne'] = scaler.fit_transform(df[['colonne']])
```

### **Q4** : Comment calculer la corrélation entre deux colonnes ?
**Réponse** :
```python
df['col1'].corr(df['col2'])
```

### **Q5** : Comment appliquer une fonction à une colonne avec `pandas` ?
**Réponse** :
```python
df['colonne'] = df['colonne'].apply(lambda x: x*2)
```

---

## **2. Machine Learning (ML)**
### **Q6** : Quelle est la différence entre la régression et la classification ?
**Réponse** :
- **Régression** : Prédit une valeur continue (ex : prix d’une maison).
- **Classification** : Prédit une catégorie (ex : spam/non-spam).

### **Q7** : Comment diviser un dataset en train/test avec `sklearn` ?
**Réponse** :
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

### **Q8** : Comment évaluer un modèle de classification ?
**Réponse** :
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print(accuracy_score(y_test, y_pred))
```

### **Q9** : Qu’est-ce que le surapprentissage (overfitting) et comment le réduire ?
**Réponse** :
- **Surapprentissage** : Le modèle performe bien sur les données d’entraînement mais mal sur les nouvelles données.
- **Solutions** : Utiliser la régularisation (L1/L2), la validation croisée, ou réduire la complexité du modèle.

### **Q10** : Comment entraîner un modèle de régression linéaire avec `sklearn` ?
**Réponse** :
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

---

## **3. Deep Learning**
### **Q11** : Quelle est la différence entre un neurone et un perceptron ?
**Réponse** :
- **Perceptron** : Modèle binaire (sortie 0 ou 1).
- **Neurone** : Peut avoir une sortie continue grâce à une fonction d’activation (ex : ReLU, sigmoïde).

### **Q12** : Comment créer un modèle séquentiel avec `Keras` ?
**Réponse** :
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])
```

### **Q13** : Qu’est-ce qu’une fonction d’activation ?
**Réponse** :
Une fonction non linéaire appliquée à la sortie d’un neurone (ex : ReLU, sigmoïde, tanh).

### **Q14** : Comment entraîner un modèle avec `Keras` ?
**Réponse** :
```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

### **Q15** : Qu’est-ce que le "vanishing gradient" et comment l’éviter ?
**Réponse** :
- **Vanishing Gradient** : Les gradients deviennent très petits pendant la rétropropagation, empêchant l’apprentissage.
- **Solutions** : Utiliser ReLU, des architectures comme ResNet, ou l’initialisation Xavier/He.

---

## **4. NLP (Natural Language Processing)**
### **Q16** : Comment tokeniser un texte avec `NLTK` ?
**Réponse** :
```python
from nltk.tokenize import word_tokenize
tokens = word_tokenize("Bonjour le monde")
```

### **Q17** : Qu’est-ce qu’un "word embedding" ?
**Réponse** :
Une représentation vectorielle dense des mots (ex : Word2Vec, GloVe).

### **Q18** : Comment utiliser `TF-IDF` avec `sklearn` ?
**Réponse** :
```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
```

### **Q19** : Qu’est-ce qu’un modèle de langage (ex : BERT) ?
**Réponse** :
Un modèle pré-entraîné sur un grand corpus pour comprendre le contexte des mots.

### **Q20** : Comment fine-tuner un modèle BERT avec `HuggingFace` ?
**Réponse** :
```python
from transformers import BertTokenizer, BertForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
```

---

## **5. Computer Vision**
### **Q21** : Comment charger une image avec `OpenCV` ?
**Réponse** :
```python
import cv2
img = cv2.imread("image.jpg")
```

### **Q22** : Qu’est-ce qu’un CNN (Convolutional Neural Network) ?
**Réponse** :
Un type de réseau de neurones spécialisé pour le traitement d’images, utilisant des couches de convolution.

### **Q23** : Comment entraîner un CNN avec `Keras` ?
**Réponse** :
```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(10, activation='softmax')
])
```

### **Q24** : Qu’est-ce que le "data augmentation" ?
**Réponse** :
Une technique pour augmenter artificiellement la taille d’un dataset en appliquant des transformations (rotation, zoom, etc.).

### **Q25** : Comment appliquer du data augmentation avec `Keras` ?
**Réponse** :
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(rotation_range=20, width_shift_range=0.2)
```

---

## **6. MLOps**
### **Q26** : Qu’est-ce que MLOps ?
**Réponse** :
Une pratique pour déployer, surveiller et maintenir des modèles ML en production.

### **Q27** : Comment sauvegarder un modèle entraîné avec `sklearn` ?
**Réponse** :
```python
import joblib
joblib.dump(model, "modele.pkl")
```

### **Q28** : Comment déployer un modèle avec `Flask` ?
**Réponse** :
```python
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})
```

### **Q29** : Qu’est-ce qu’un "pipeline ML" ?
**Réponse** :
Une séquence d’étapes pour prétraiter les données, entraîner un modèle, et faire des prédictions.

### **Q30** : Comment automatiser un pipeline avec `Airflow` ?
**Réponse** :
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
dag = DAG('ml_pipeline', schedule_interval='@daily')
train_task = PythonOperator(task_id='train_model', python_callable=train_model, dag=dag)
```

---

## **7. Big Data & Outils**
### **Q31** : Qu’est-ce qu’un DataFrame `Spark` ?
**Réponse** :
Une structure de données distribuée pour le traitement de grandes quantités de données.

### **Q32** : Comment lire un fichier avec `PySpark` ?
**Réponse** :
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()
df = spark.read.csv("fichier.csv", header=True)
```

### **Q33** : Qu’est-ce que `Dask` ?
**Réponse** :
Une bibliothèque pour le calcul parallèle en Python, compatible avec `pandas` et `numpy`.

### **Q34** : Comment utiliser `Dask` pour paralléliser un calcul ?
**Réponse** :
```python
import dask.dataframe as dd
ddf = dd.read_csv("fichier.csv")
result = ddf.groupby('colonne').mean().compute()
```

### **Q35** : Qu’est-ce que `Hadoop` et `HDFS` ?
**Réponse** :
- **Hadoop** : Framework pour le stockage et le traitement distribué de données.
- **HDFS** : Système de fichiers distribué utilisé par Hadoop.

---

## **8. Statistiques & Mathématiques**
### **Q36** : Qu’est-ce que la p-value ?
**Réponse** :
Une mesure pour évaluer la significativité statistique d’un résultat (hypothèse nulle).

### **Q37** : Comment calculer un intervalle de confiance ?
**Réponse** :
```python
from scipy import stats
stats.norm.interval(0.95, loc=mean, scale=std_error)
```

### **Q38** : Qu’est-ce que la "loi des grands nombres" ?
**Réponse** :
Plus l’échantillon est grand, plus la moyenne de l’échantillon se rapproche de la moyenne réelle.

### **Q39** : Comment calculer la matrice de confusion ?
**Réponse** :
```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
```

### **Q40** : Qu’est-ce que le "bias-variance tradeoff" ?
**Réponse** :
Un équilibre entre :
- **Bias** : Erreur due à une hypothèse trop simpliste.
- **Variance** : Erreur due à une sensibilité excessive aux données d’entraînement.

---