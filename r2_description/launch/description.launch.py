import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.descriptions import ParameterValue

def generate_launch_description():

    urdf = os.path.join(
        get_package_share_directory('r2_description'),'urdf',
        'r2.urdf.xacro')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': ParameterValue(
                Command(['xacro ', str(urdf)]), value_type=str
            )
        }]
        )
    ])
