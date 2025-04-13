# Install script for directory: /media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/src/tutorial

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial/msg" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/src/tutorial/msg/Position.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial/srv" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/src/tutorial/srv/multiplier.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial/cmake" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/tutorial-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/devel/include/tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/devel/share/common-lisp/ros/tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/devel/lib/python3/dist-packages/tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/devel/lib/python3/dist-packages/tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/tutorial.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial/cmake" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/tutorial-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial/cmake" TYPE FILE FILES
    "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/tutorialConfig.cmake"
    "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/tutorialConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tutorial" TYPE FILE FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/src/tutorial/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/tutorial" TYPE PROGRAM FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/publisher_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/tutorial" TYPE PROGRAM FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/subscriber_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/tutorial" TYPE PROGRAM FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/service_server_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/tutorial" TYPE PROGRAM FILES "/media/fabienfrfr/F6166FAF166F7013/0_JOBS/ROBOT/RosWebGame/build/tutorial/catkin_generated/installspace/service_client_node.py")
endif()

