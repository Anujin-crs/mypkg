from launch
import LaunchDescription
import launch.actions
import launch.substitutions
from launch_ros.actions
import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            namespace='turtle1',
            executable='talker',
            name = 'node1'
        ),
        Node(
            package='mypkg',
            namespace='turtle2',
            executable='listener',
            name = 'node2'
            parameters=[
                      {"background_r": 1.0},
                      {"background_r": 2.0},
                      {"background_r": 0.2}
                       ]
        ),

    ])  
