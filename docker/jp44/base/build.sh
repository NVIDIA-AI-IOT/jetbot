CONTAINER=jetbot:jp44-base

cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ./

sudo docker build -t jetbot:jp44-base -f Dockerfile .

