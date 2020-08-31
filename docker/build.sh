export JETBOT_VERSION=jp44

DOCKER_JSON_FILE="/etc/docker/daemon.json"
if ! grep -Fq "default-runtime" $DOCKER_JSON_FILE; then
    sudo sed -i 's/^}/    ,\n    \"default-runtime\": \"nvidia\"\n}/' $DOCKER_JSON_FILE
    echo "Restarting docker daemon ..."
    sudo systemctl restart docker
fi

cd base && ./build.sh && cd ..
cd models && ./build.sh && cd ..
cd display && ./build.sh && cd ..
cd jupyter && ./build.sh && cd ..
cd camera && ./build.sh && cd ..
