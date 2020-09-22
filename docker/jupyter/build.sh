sudo docker build \
    --build-arg BASE_IMAGE=jetbot:models-$JETBOT_VERSION-$L4T_VERSION \
    -t jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION \
    -f Dockerfile .
