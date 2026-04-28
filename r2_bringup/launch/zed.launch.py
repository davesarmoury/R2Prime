import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python import get_package_share_directory
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    zed_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare("zed_wrapper"), "launch", "zed_camera.launch.py"])]
        ),
        launch_arguments={
            "camera_name": "zedxm",
            "camera_model": "zedxm",
            "publish_tf": "false",
            "publish_urdf": "false",
            "ros_params_override_path": os.path.join(get_package_share_directory('r2_bringup'), 'config', 'zedxm.yaml'),
        }.items(),
    )

    launches = [
        zed_launch,
    ]

    return LaunchDescription(launches)
