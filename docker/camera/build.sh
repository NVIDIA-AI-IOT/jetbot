sudo docker build \
    --build-arg BASE_IMAGE=jetbot-base:$JETBOT_VERSION \
    -t jetbot-camera:$JETBOT_VERSION \
    -f Dockerfile .