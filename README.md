# franka_gazebo
A simple ROS Gazebo package for Franka Panda robot arm.

Original URDF/XACRO description files and robot meshes were taken from official Franka Emika [github repo](https://github.com/frankaemika/franka_ros).
This package adds missing inertial and gazebo-specific tags to URDF/XACRO descriptions so Panda can be simulated in Gazebo.

### Calculating inertial properties
[MeshLab](http://www.meshlab.net/) was used to calculate inertial properties (volume, center of mass and inertia tensor) of each link using provided 3D models.
For instructions on how to do this, see this [tutorial](http://gazebosim.org/tutorials?tut=inertia).

In order to get higher accuracy inertial properties, each link was scaled by a factor of 10 before calculation.

Some of the provided meshes had errors that prevented inertial properties to be calculated.
If that happens, try to apply the following filters:
1. `Filters` > `Cleaning and Repairing` > `Merge close vertices`
2. `Filters` > `Cleaning and Repairing` > `Remove duplicate face`
3. `Filters` > `Cleaning and Repairing` > `Remove duplicate vertex`
4. `Filters` > `Remeshing, Simplification and Reconstruction` > `Close holes`

After applying each of the filters, try to calculate inertias. Often, even the first filter fixes the problem.

Mass of each link was calculated like this: `mass of the link` = `volume of the link` / `total volume` * `total mass`

Total mass is 18 kg (from the [offical datasheet](https://s3-eu-central-1.amazonaws.com/franka-de-uploads-staging/uploads/2018/05/2018-05-datasheet-panda.pdf)), and the total volume is calculated by adding volumes of each link.

There is a [python script](./scripts/inertial_xml_maker.py) where you can enter inertial data calculated by MeshLab along with used scaling factor
and it will print out XML style inertial tags that can be copied directly to URDF/XACRO file.

### Using Franka Panda in Gazebo

It is also possible to move Panda arm in Gazebo thanks to the [position_controllers/JointPositionController](https://github.com/ros-controls/ros_controllers/tree/melodic-devel/position_controllers) in each joint.
PID parameters were set to enable stable control, but they can be further optimized.

Two launch files are provided in this package, one for just the arm and the other for the arm with the attached gripper.
They spawn the robot model in Gazebo and start the controllers.

Launch file `panda_arm_hand.launch` includes an example controller that sends sinusoidal position commands to each joint.
Make sure that Gazebo is already running by launching your desired world, for example:

`roslaunch gazebo_ros empty_world.launch`.
