CONTAINER=jetbot-deps:jp44

cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc ./

sudo docker build -t jetbot-deps:jp44 -f Dockerfile .

