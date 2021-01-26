#!/bin/bash

sudo docker push jetbot/jetbot:camera-$JETBOT_VERSION-$L4T_VERSION
sudo docker push jetbot/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION
sudo docker push jetbot/jetbot:display-$JETBOT_VERSION-$L4T_VERSION
