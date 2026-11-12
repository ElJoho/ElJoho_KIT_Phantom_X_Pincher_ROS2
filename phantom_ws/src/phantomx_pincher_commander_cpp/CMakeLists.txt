cmake_minimum_required(VERSION 3.8)
project(phantomx_pincher_commander_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(phantomx_pincher_interfaces REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(test_moveit src/test_moveit.cpp)
target_link_libraries(test_moveit
  ${rclcpp_TARGETS}
  ${moveit_ros_planning_interface_TARGETS}
)

add_executable(commander src/commander_template.cpp)
target_link_libraries(commander
  ${rclcpp_TARGETS}
  ${moveit_ros_planning_interface_TARGETS}
  ${example_interfaces_TARGETS}
  ${phantomx_pincher_interfaces_TARGETS}
  ${std_msgs_TARGETS}
)

install(TARGETS
  test_moveit
  commander
  DESTINATION lib/${PROJECT_NAME}/
)

ament_package()
