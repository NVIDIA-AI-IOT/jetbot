#!/bin/bash

set -e

password='jetbot'

# Record the time this script starts
date

# Get the full dir name of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Keep updating the existing sudo time stamp
sudo -v
while true; do sudo -n true; sleep 120; kill -0 "$$" || exit; done 2>/dev/null &

# Enable i2c permissions
echo -e "\e[100m Enable i2c permissions \e[0m"
sudo usermod -aG i2c $USER

# Install pip and some python dependencies
echo -e "\e[104m Install pip and some python dependencies \e[0m"
sudo apt-get update
sudo apt install -y python3-pip python3-pil
sudo -H pip3 install Cython
sudo -H pip3 install --upgrade numpy

# Install jtop
echo -e "\e[100m Install jtop \e[0m"
sudo -H pip3 install jetson-stats 


# Install the pre-built TensorFlow pip wheel
echo -e "\e[48;5;202m Install the pre-built TensorFlow pip wheel \e[0m"
sudo apt-get update
sudo apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
sudo apt-get install -y python3-pip
sudo -H pip3 install -U pip setuptools
sudo -H pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker six mock requests gast h5py astor termcolor protobuf keras-applications keras-preprocessing wrapt google-pasta
sudo -H pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 tensorflow==1.15.2+nv20.4

# Install the pre-built PyTorch pip wheel 
echo -e "\e[45m Install the pre-built PyTorch pip wheel  \e[0m"
cd
wget -N https://nvidia.box.com/shared/static/3ibazbiwtkl181n95n9em3wtrca7tdzp.whl -O torch-1.5.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install -y python3-pip libopenblas-base libopenmpi-dev 
sudo -H pip3 install Cython
sudo -H pip3 install numpy torch-1.5.0-cp36-cp36m-linux_aarch64.whl

# Install torchvision package
echo -e "\e[45m Install torchvision package \e[0m"
cd
git clone https://github.com/pytorch/vision
cd vision
#git checkout v0.4.0
sudo -H python3 setup.py install

# Install traitlets (master, to support the unlink() method)
echo -e "\e[48;5;172m Install traitlets \e[0m"
sudo python3 -m pip install git+https://github.com/ipython/traitlets@master

# Install jupyter lab
echo -e "\e[48;5;172m Install Jupyter Lab \e[0m"
sudo apt install -y curl
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs 
sudo -H pip3 install jupyter jupyterlab
sudo -H jupyter labextension install @jupyter-widgets/jupyterlab-manager

jupyter lab --generate-config
python3 -c "from notebook.auth.security import set_password; set_password('$password', '$HOME/.jupyter/jupyter_notebook_config.json')"

# fix for permission error
sudo chown -R jetbot:jetbot ~/.local/share/

# install jetbot python module
cd
sudo apt install -y python3-smbus
cd ~/jetbot
sudo apt-get install -y cmake
sudo python3 setup.py install 

# Install jetbot services
cd jetbot/utils
python3 create_stats_service.py
sudo mv jetbot_stats.service /etc/systemd/system/jetbot_stats.service
sudo systemctl enable jetbot_stats
sudo systemctl start jetbot_stats
python3 create_jupyter_service.py
sudo mv jetbot_jupyter.service /etc/systemd/system/jetbot_jupyter.service
sudo systemctl enable jetbot_jupyter
sudo systemctl start jetbot_jupyter

# Make swapfile
cd 
sudo fallocate -l 4G /var/swapfile
sudo chmod 600 /var/swapfile
sudo mkswap /var/swapfile
sudo swapon /var/swapfile
sudo bash -c 'echo "/var/swapfile swap swap defaults 0 0" >> /etc/fstab'

# Copy JetBot notebooks to home directory
cp -r ~/jetbot/notebooks ~/Notebooks

echo -e "\e[42m All done! \e[0m"

#record the time this script ends
date
