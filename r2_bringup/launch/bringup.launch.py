from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    desc_launch = IncludeLaunchDescription(PathJoinSubstitution([PathJoinSubstitution([FindPackageShare('r2_description'), 'launch']), 'description.launch.py']))
    control_launch = IncludeLaunchDescription(PathJoinSubstitution([PathJoinSubstitution([FindPackageShare('r2_control'), 'launch']), 'r2_control.launch.py']))

    # Return the LaunchDescription
    return LaunchDescription([
        desc_launch,
        control_launch,
    ])
