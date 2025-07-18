# # =================== START: THIS IS THE FINAL CORRECT setup.py ===================
# from setuptools import find_packages, setup

# package_name = 'b3rb_ros_aim_india'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=find_packages(exclude=['test']),
#     data_files=[
#         # This line installs the package manifest
#         ('share/' + package_name, ['package.xml']),
#         # These lines install our data files TO THE CORRECT LOCATION
#         ('share/' + package_name, ['resource/coco.yaml']),
#         ('share/' + package_name, ['resource/yolov5n-int8.tflite']),
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='mayank',
#     maintainer_email='mayankmahajan.x@nxp.com',
#     description='NXP B3RB Warehouse Challenge',
#     license='Apache-2.0',
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': [
#                 'explore = b3rb_ros_aim_india.b3rb_ros_warehouse:main',
#                 'visualize = b3rb_ros_aim_india.b3rb_ros_draw_map:main',
#                 'remover = b3rb_ros_aim_india.b3rb_ros_model_remove:main',
#                 'detect = b3rb_ros_aim_india.b3rb_ros_object_recog:main',
#         ],
#     },
# )
# # =================== END: THIS IS THE FINAL CORRECT setup.py ===================


from setuptools import find_packages, setup

package_name = 'b3rb_ros_aim_india'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/ament_index/resource_index', ['resource/coco.yaml']),
        ('share/ament_index/resource_index', ['resource/yolov5n-int8.tflite']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mayank',
    maintainer_email='mayankmahajan.x@nxp.com',
    description='MR-B3RB Line Follower',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'explore = b3rb_ros_aim_india.b3rb_ros_warehouse:main',
                'visualize = b3rb_ros_aim_india.b3rb_ros_draw_map:main',
                'remover = b3rb_ros_aim_india.b3rb_ros_model_remove:main',
                'detect = b3rb_ros_aim_india.b3rb_ros_object_recog:main',
        ],
    },
)