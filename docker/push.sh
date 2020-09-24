#!/bin/bash

sudo docker push $JETBOT_DOCKER_REMOTE/jetbot:camera-$JETBOT_VERSION-$L4T_VERSION
sudo docker push $JETBOT_DOCKER_REMOTE/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION
sudo docker push $JETBOT_DOCKER_REMOTE/jetbot:display-$JETBOT_VERSION-$L4T_VERSION
