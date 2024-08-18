import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640, 480],  # Reduced resolution
                'camera_frame_id': 'camera_link_optical',
                'framerate': 15  # Lower frame rate
            }]
        ),
        Node(
            package='image_transport',
            executable='republish',
            name='republish_compressed',
            remappings=[('in', '/camera/image_raw'), ('out', '/camera/image/compressed')],
            parameters=[{
                'jpeg_quality': 50  # Adjusted JPEG quality
            }]
        ),
    ])

