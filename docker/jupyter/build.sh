sudo docker build \
    --build-arg BASE_IMAGE=jetbot-base:$JETBOT_VERSION \
    -t jetbot-jupyter:$JETBOT_VERSION \
    -f Dockerfile .