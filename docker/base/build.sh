cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ../.. # copy to jetbot root

sudo docker build \
    -t jetbot-base:$JETBOT_VERSION \
    -f Dockerfile \
    ../..  # jetbot repo root as context

