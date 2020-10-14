# Collision Avoidance 

In this example we'll collect an *image classification* dataset that will be used to help keep
JetBot safe!  We'll teach JetBot to detect two scenarios ``free`` and ``blocked``.  We'll use this AI classifier to prevent JetBot from entering dangerous territory.

[![](http://img.youtube.com/vi/6cLk9TSgFSw/0.jpg)](http://www.youtube.com/watch?v=6cLk9TSgFSw "Launching of JetBots")

#### Step 1 - Collect data on JetBot

<a href="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03a_Data-Collection.png"><img src="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03a_Data-Collection.png" height="320"></a>

1. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``
2. Sign in with the default password ``jetbot``
2. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
3. Navigate to ``~/Notebooks/collision_avoidance/``
4. Open and follow the [``data_collection.ipynb``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/collision_avoidance/data_collection.ipynb) notebook

???+ tip 
    We provide a [pre-trained model](https://drive.google.com/open?id=1UsRax8bR3R-e-0-80KfH2zAt-IyRPtnW) so you can skip to step 3 if desired.  This model was trained on a limited dataset using the Raspberry Pi V2 Camera with wide angle attachment.

#### Step 2 - Train neural network

<a href="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03b_Training.png"><img src="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03b_Training.png" height="320"></a>

##### Option 1 - Train on Jetson Nano
1. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``
2. Sign in with the default password ``jetbot``
3. In the Jupyter Lab tab, navigate to ``~/collision_avoidance``
5. Open and follow the [``train_model_resnet18.ipynb``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/collision_avoidance/data_collection.ipynb) notebook

##### Option 2 - Train on other GPU machine
1. Connect to a GPU machine with PyTorch installed and a Jupyter Lab server running
2. Upload the collision avoidance [training notebook](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/collision_avoidance/train_model_resnet18.ipynb) to this machine
3. Open and follow the ``train_model_resnet18.ipynb`` notebook


#### Step 3 - Optimize the model on Jetson Nano

1. Connect to your robot by navigating to ``https://<jetbot_ip_address>:8888``
2. Sign in with the default password jetbot
3. Shutdown all other running notebooks by selecting Kernel -> Shutdown All Kernels...
4. Navigate to ``~/Notebooks/road_following``
5. Open and follow the [``live_demo_resnet18_build_trt.ipynb``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/collision_avoidance/live_demo_resnet18_build_trt.ipynb) notebook to optimize the model with TensorRT

#### Step 4 - Run live demo on JetBot

<a href="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03c_Live-demo.png"><img src="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL03c_Live-demo.png" height="320"></a>

1. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``
2. Sign in with the default password ``jetbot``
3. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
4. Navigate to ``~/Notebooks/collision_avoidance``
5. Open and follow the [``live_demo_resnet18_trt.ipynb``](https://github.com/NVIDIA-AI-IOT/jetbot/blob/master/notebooks/collision_avoidance/live_demo_resnet18_trt.ipynb) notebook to run the optimized model


???+ caution   
    JetBot will physically move in this notebook, make sure it has enough space to move around.

