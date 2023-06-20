import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    aruco_params = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'config',
        'aruco_parameters.yaml'
        )
    
    camera_param = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'config',
        'camera_param.yaml'
        )
    
    aruco_node = Node(
        package='ros2_aruco',
        executable='aruco_node',
        parameters=[aruco_params]
    )
    camera_node = Node(
        package='usb_cam', executable='usb_cam_node_exe', output='screen',
        name="camera_node",
        # namespace=ns,
        parameters=[camera_param]
    )
    return LaunchDescription([
        aruco_node,
        camera_node
    ])
