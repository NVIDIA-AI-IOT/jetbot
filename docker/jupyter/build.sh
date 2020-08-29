sudo docker build \
    --build-arg BASE_IMAGE=jetbot-models:$JETBOT_VERSION \
    -t jetbot-jupyter:$JETBOT_VERSION \
    -f Dockerfile .
