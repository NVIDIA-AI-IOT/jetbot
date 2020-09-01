# Road Following

In this example we'll collect an *image regression* dataset that will enable JetBot to follow a road!  We'll teach JetBot to detect a target ``x, y`` image coordinate that the JetBot will chase.  As JetBot gets closer to the point, it moves further along the track.

#### Step 1 - Collect data on JetBot

<a href="images/JL03a_Data-Collection.png"><img src="images/JL03a_Data-Collection.png" height="320"></a>

1. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``

2. Sign in with the default password ``jetbot``
2. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
3. Navigate to ``~/Notebooks/road_following/``
4. Open and follow the ``data_collection.ipynb`` notebook

#### Step 2 - Train neural network

##### Option 1 - Train on Jetson nano
1. Shutdown your robot and remove the micro USB power cable.

2. Power the Jetson Nano by using the 5V wall power supply.
3. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``
4. Sign in with the default password ``jetbot``
5. In the Jupyter Lab tab, navigate to ``~/Notebooks/road_following``
6. Upload the road following avoidance [training notebook](#) to this folder
7. Open and follow the ``train_model.ipynb`` notebook

##### Option 2 - Train on other GPU machine
1. Connect to a GPU machine with PyTorch installed and a Jupyter Lab server running

2. Upload the road following avoidance [training notebook](#) to this machine
3. Open and follow the ``train_model.ipynb`` notebook

#### Step 3 - Run live demo on JetBot

<a href="images/JL03c_Live-demo.png"><img src="images/JL03c_Live-demo.png" height="320"></a>

1. Power your robot from the USB battery pack

2. Connect back to your robot by navigating to ``http://<jetbot_ip_address>:8888``
3. Sign in with the default password ``jetbot``
4. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
5. Navigate to ``~/Notebooks/road_following``
6. Open and follow the ``live_demo.ipynb`` notebook
    > Start cautious and give JetBot enough space to move around.
