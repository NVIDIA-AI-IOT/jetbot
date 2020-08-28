export JETBOT_VERSION=jp44

JUPYTER_WORKSPACE=$1

./display/enable.sh
./camera/enable.sh
./jupyter/enable.sh $JUPYTER_WORKSPACE
