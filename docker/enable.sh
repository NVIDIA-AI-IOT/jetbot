source configure.sh

JUPYTER_WORKSPACE=${1:-$HOME}  # default to $HOME
JETBOT_CAMERA=${2:-opencv_gst_camera}  # default to opencv

if [ "$JETBOT_CAMERA" = "zmq_camera" ]
then
	./camera/enable.sh
fi

./display/enable.sh
./jupyter/enable.sh $JUPYTER_WORKSPACE $JETBOT_CAMERA
