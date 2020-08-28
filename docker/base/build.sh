cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ./

sudo docker build \
    -t jetbot-base:$JETBOT_VERSION \
    -f Dockerfile \
    ../..  # jetbot repo root as context

