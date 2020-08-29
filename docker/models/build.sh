sudo docker build \
    --build-arg BASE_IMAGE=jetbot-base:$JETBOT_VERSION \
    -t jetbot-models:$JETBOT_VERSION \
    -f Dockerfile .
