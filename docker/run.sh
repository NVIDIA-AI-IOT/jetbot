export JETBOT_VERSION=jp44

JUPYTER_WORKSPACE=$1

./display/run.sh
./camera/run.sh
./jupyter/run.sh $JUPYTER_WORKSPACE