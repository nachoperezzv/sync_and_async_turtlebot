# Multiple robots in simulation with ROS

Multi-robot systems project in which two tasks are requested: perform a movement of four turtlebots synchronously and asynchronously

## Structure of the document

Here it is a ros package called *multi_ws*, where you will find it's *CMakeLists.txt* & *package.xml*. There're also three more directories: *include* (which is empty), *launch* (where the *.launch files are located) and *src* (where are the scripts of the two nodes required for the tasks) 


## Requirements

In order to use the turtlebot 2, it has been used the *tb2_ws* workspace, which contains the needed worlds, .urdf files, etc, to run the turtlebot. The ros package created is located inside of this workspace, so it's unknownn if creating the package outside of this workspace will work. 


## To run the project

Once you have created your package *multi_ws* inside *tb2_ws* workspace: 
```
catkin_create_pkg multi_ws rospy std_msgs
```

Make sure to do:
```
source devel_isolated/setup.bash
```

Then, in order to launch *Gazebo* you will have to execute: 
```
roslaunch multi_ws main.launch
```

There's the option of editing this *main.launch* so the node are launched automatically. The code is commented and you only will have to undo that. After Gazebo is running, open a new terminal in *src/* directorie and choose which task you want to accomplish.

If you want synchronous motion:
```
python p1-all-at-once.py
```

Or if you want asynchronus motion: 
```
python p1-sequential.py
```
