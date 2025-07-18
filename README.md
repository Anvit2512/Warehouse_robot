🚀 STEP 1: Install CogniPilot AIRY Release (Includes ROS 2 + Gazebo + All Dependencies)
🔧 Run these commands in terminal:

sudo apt-get update
sudo apt-get install git wget -y

📁 Create installer directory:

mkdir -p ~/cognipilot/installer

📥 Download installer script:

wget -O ~/cognipilot/installer/install_cognipilot.sh https://raw.githubusercontent.com/CogniPilot/helmet/main/install/install_cognipilot.sh

🛠 Make it executable:

chmod a+x ~/cognipilot/installer/install_cognipilot.sh

▶ Run installer:

/bin/bash ~/cognipilot/installer/install_cognipilot.sh

📌 During installation:

    Select 1 (airy) when asked for release

    Select 1 (native) for installer type

    Say Y to continue installing packages

    Say n when asked about SSH keys

🧱 STEP 2: Build Base Workspace
📥 Source environment and build:

source ~/.profile
source ~/.bashrc
build_workspace

💡 When prompted:

    Say n (No) for using ssh keys

    Select 1 (b3rb) as platform

👇 Finally:

source ~/.bashrc

🖼 STEP 3: Build Foxglove (Optional Visual Debugging)

build_foxglove

    Select n (No) for SSH keys

    Select 1 (airy) for release

📁 STEP 4: Set Up NXP_AIM_INDIA_2025 and YOLOv5
Clone the challenge repo:

cd ~/cognipilot/cranium/src/
git clone https://github.com/NXPHoverGames/NXP_AIM_INDIA_2025.git

Clone YOLOv5 repo:

git clone https://github.com/NXPHoverGames/B3RB_YOLO_OBJECT_RECOG.git
cd B3RB_YOLO_OBJECT_RECOG
git checkout nxp_aim_india_2025

Move necessary files:

mv resource/coco.yaml ~/cognipilot/cranium/src/NXP_AIM_INDIA_2025/resource/
mv resource/yolov5n-int8.tflite ~/cognipilot/cranium/src/NXP_AIM_INDIA_2025/resource/
mv b3rb_ros_aim_india/b3rb_ros_object_recog.py ~/cognipilot/cranium/src/NXP_AIM_INDIA_2025/b3rb_ros_aim_india/
cd ..
rm -rf B3RB_YOLO_OBJECT_RECOG

Edit setup.py:

Uncomment lines 12, 13, and 28 in:

~/cognipilot/cranium/src/NXP_AIM_INDIA_2025/setup.py

🌐 STEP 5: Clone Remaining Required Repos

cd ~/cognipilot/cranium/src/
rm -rf dream_world synapse_msgs b3rb_simulator

Clone new versions:

git clone https://github.com/NXPHoverGames/dream_world.git
cd dream_world && git checkout nxp_aim_india_2025
cd ..

git clone https://github.com/NXPHoverGames/synapse_msgs.git
cd synapse_msgs && git checkout nxp_aim_india_2025
cd ..

git clone https://github.com/NXPHoverGames/b3rb_simulator.git
cd b3rb_simulator && git checkout nxp_aim_india_2025

📦 STEP 6: Install Python Dependencies (Allowed Libraries Only)

pip install \
    torch==2.3.0 \
    torchvision==0.18.0 \
    numpy==1.26.4 \
    opencv-python==4.11.0.86 \
    scipy==1.15.1 \
    scikit-learn==1.5.2 \
    tk==0.1.0 \
    pyzbar==0.1.9 \
    matplotlib==3.5.1 \
    pyyaml==6.0.2 \
    tflite-runtime==2.14.0

🧪 STEP 7: Build Final Workspace

cd ~/cognipilot/cranium/
colcon build
source install/setup.bash

🎮 STEP 8: Launch Simulation (Pick Any Warehouse)
Example for warehouse_1 (replace for 2/3/4):

ros2 launch b3rb_gz_bringup sil.launch.py \
    world:=nxp_aim_india_2025/warehouse_1 \
    warehouse_id:=1 shelf_count:=2 \
    initial_angle:=135.0 \
    x:=0.0 y:=0.0 yaw:=0.0

Other examples:

ros2 launch b3rb_gz_bringup sil.launch.py world:=nxp_aim_india_2025/warehouse_2 warehouse_id:=2 shelf_count:=4 initial_angle:=040.6 x:=0.0 y:=-7.0 yaw:=1.57
ros2 launch b3rb_gz_bringup sil.launch.py world:=nxp_aim_india_2025/warehouse_3 warehouse_id:=3 shelf_count:=3 initial_angle:=045.0 x:=5.0 y:=-2.0 yaw:=3.14
ros2 launch b3rb_gz_bringup sil.launch.py world:=nxp_aim_india_2025/warehouse_4 warehouse_id:=4 shelf_count:=5 initial_angle:=045.0 x:=5.0 y:=-2.0 yaw:=3.14

⚠ If you see errors like simulation not starting or /cerebri/out/status stuck on "Waiting", cancel all and try again from Step 7.
🗺 OPTIONAL: View SLAM Map

source ~/cognipilot/cranium/install/setup.bash
ros2 run b3rb_ros_aim_india visualize

🧠 OPTIONAL: Use Foxglove for Debugging
Clone:

cd ~/cognipilot/electrode/src/
rm -rf electrode
git clone https://github.com/NXPHoverGames/electrode.git
cd electrode
git checkout nxp_aim_india_2025

Build:

cd ~/cognipilot/electrode/
colcon build
source install/setup.bash

Launch Foxglove:

ros2 launch electrode electrode.launch.py sim:=True

    Open Foxglove Studio

    Connect using WebSocket URL: ws://localhost:8765

    Load layout: ~/cognipilot/electrode/src/electrode/foxglove_layouts/b3rb.json

✅ YOU ARE NOW SET UP!

Let me know if you want:

    A ready-made bash file to execute all common commands

    A project boilerplate for b3rb_ros_warehouse.py

    Help understanding how to write the shelf detection or navigation logic

You're almost ready to start development and testing!
