sudo docker run -it -d \
    --restart always \
    --runtime nvidia \
    --network host \
    --privileged \
    --name=jetbot_display \
    jetbot-display:$JETBOT_VERSION