# Collision Avoidance 

In this example we'll collect an *image classification* dataset that will be used to help keep
JetBot safe!  We'll teach JetBot to detect two scenarios ``free`` and ``blocked``.  We'll use this AI classifier to prevent JetBot from entering dangerous territory.

[![](http://img.youtube.com/vi/6cLk9TSgFSw/0.jpg)](http://www.youtube.com/watch?v=6cLk9TSgFSw "Launching of JetBots")

#### Step 1 - Collect data on JetBot

> We provide a [pre-trained model](https://drive.google.com/open?id=1UsRax8bR3R-e-0-80KfH2zAt-IyRPtnW) so you can skip to step 3 if desired.  This model was trained on a limited dataset using the Raspberry Pi V2 Camera with wide angle attachment.

<a href="images/JL03a_Data-Collection.png"><img src="images/JL03a_Data-Collection.png" height="320"></a>

1. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``

2. Sign in with the default password ``jetbot``
2. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
3. Navigate to ``~/Notebooks/collision_avoidance/``
4. Open and follow the ``data_collection.ipynb`` notebook

#### Step 2 - Train neural network

<a href="images/JL03b_Training.png"><img src="images/JL03b_Training.png" height="320"></a>

##### Option 1 - Train on Jetson nano
1. Shutdown your robot and remove the micro USB power cable.

2. Power the Jetson Nano by using the 5V wall power supply.
3. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``
4. Sign in with the default password ``jetbot``
5. In the Jupyter Lab tab, navigate to ``~/collision_avoidance``
6. Upload the collision avoidance [training notebook](../../jetbot/blob/master/notebooks/collision_avoidance/train_model.ipynb) to this folder
7. Open and follow the ``train_model.ipynb`` notebook

##### Option 2 - Train on other GPU machine
1. Connect to a GPU machine with PyTorch installed and a Jupyter Lab server running

2. Upload the collision avoidance [training notebook](../../jetbot/blob/master/notebooks/collision_avoidance/train_model.ipynb) to this machine
3. Open and follow the ``train_model.ipynb`` notebook

#### Step 3 - Run live demo on JetBot

<a href="images/JL03c_Live-demo.png"><img src="images/JL03c_Live-demo.png" height="320"></a>

1. Power your robot from the USB battery pack

2. Connect back to your robot by navigating to ``http://<jetbot_ip_address>:8888``
3. Sign in with the default password ``jetbot``
4. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
5. Navigate to ``~/Notebooks/collision_avoidance``
6. Open and follow the ``live_demo.ipynb`` notebook
    > Start cautious and give JetBot enough space to move around.