from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    filepath_config_joy = PathJoinSubstitution(
        [FindPackageShare('r2_control'), 'config', ('teleop.yaml')]
    )

    node_joy = Node(
        package='joy',
        executable='joy_node',
        output='screen',
        name='joy_node',
        parameters=[filepath_config_joy]
    )

    node_teleop_twist_joy = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        output='screen',
        name='teleop_twist_joy_node',
        parameters=[filepath_config_joy],
        remappings=[
            ('cmd_vel', '/diff_drive_controller/cmd_vel'),
        ],
    )


    ld = LaunchDescription()
    ld.add_action(node_joy)
    ld.add_action(node_teleop_twist_joy)
    return ld
