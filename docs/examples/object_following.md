# Object Following

In this example we'll have JetBot follow an object using a pre-trained model capable of detecting common objects like``Person``, ``Cup``, and ``Dog``.  While doing this, JetBot will run the collision avoidance model from Example 3 to make sure it stays safe!

[![](http://img.youtube.com/vi/MBUEbU9Q6wg/0.jpg)](http://www.youtube.com/watch?v=MBUEbU9Q6wg "Dancing with JetBot")

???+ note
    Please note that example for now only works with the SD card image based software setup.


1. Download the object detection model according to the table below

    | JetBot SD Card Version | Model |
    |----------------|-------|
    | v0.3           | [ssd_mobilenet_v2_coco.engine](https://drive.google.com/open?id=1RnNBHPDphIOWwHCSfeMCWQ7XN3w3tKFD) |
    | v0.4 (latest)  | [ssd_mobilenet_v2_coco.engine](https://drive.google.com/open?id=1KjlDMRD8uhgQmQK-nC2CZGHFTbq4qQQH) |


<a href="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL04_Object-Following.png"><img src="https://raw.githubusercontent.com/wiki/NVIDIA-AI-IOT/jetbot/images/JL04_Object-Following.png" height="320"></a>

2. Connect to your robot by navigating to ``http://<jetbot_ip_address>:8888``

3. Shutdown all other running notebooks by selecting ``Kernel`` -> ``Shutdown All Kernels...``
4. Navigate to ``~/Notebooks/object_following/``
5. Upload the pre-trained ``ssd_mobilenet_v2_coco.engine`` model to this folder

    ???+ info
        Also make sure the collision avoidance model from Example 3 is in ``~/Notebooks/collision_avoidance``

6. Open and follow the ``live_demo.ipynb`` notebook
    
    ???+ warning
        Start cautious and give JetBot enough space to move around.


