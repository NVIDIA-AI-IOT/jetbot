sudo docker run -it -d \
    --restart always \
    --runtime nvidia \
    --network host \
    --privileged \
    --name=jetbot_display \
    jetbot/jetbot:display-$JETBOT_VERSION-$L4T_VERSION
