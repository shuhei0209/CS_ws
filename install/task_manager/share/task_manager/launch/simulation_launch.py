from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Task Manager Node
        Node(
            package='task_manager',
            executable='task_manager',
            name='task_manager_node',
            output='screen'
        ),
        # Navigation Node
        Node(
            package='navigation',
            executable='navigation_node',
            name='navigation_node',
            output='screen'
        )
    ])
