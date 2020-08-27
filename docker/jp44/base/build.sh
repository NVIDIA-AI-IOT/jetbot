ROOT=../../..  # jetbot dir

sudo docker build \
    -t jetbot-base:jp44 \
    -f Dockerfile $ROOT