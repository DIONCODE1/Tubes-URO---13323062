cmake_minimum_required(VERSION 3.5)
project(box_robot)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(
    PROGRAMS
    box_robot_node.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
