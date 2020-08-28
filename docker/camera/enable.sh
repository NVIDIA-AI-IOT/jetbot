sudo systemctl restart nvargus-daemon

sudo docker run -it -d \
    --restart always \
    --runtime nvidia \
    --network host \
    --privileged \
    --device /dev/video* \
    --volume /dev/bus/usb:/dev/bus/usb \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    --privileged \
    --name=jetbot_camera \
    jetbot-camera:$JETBOT_VERSION