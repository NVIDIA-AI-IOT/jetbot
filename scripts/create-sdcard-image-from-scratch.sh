#!/bin/bash

password='jetbot'

# Keep updating the existing sudo time stamp
sudo -v
while true; do sudo -n true; sleep 120; kill -0 "$$" || exit; done 2>/dev/null &

# Enable i2c permissions
sudo usermod -aG i2c $USER

# Install pip and some python dependencies
sudo apt-get update
sudo apt install -y python3-pip python3-pil
sudo pip3 install --upgrade numpy

# Install the pre-built TensorFlow pip wheel
sudo apt-get update
sudo apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
sudo apt-get install -y python3-pip
sudo pip3 install -U pip
sudo pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.6 enum34 futures testresources setuptools protobuf
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu==1.14.0+nv19.10

# Install the pre-built PyTorch pip wheel 
wget https://nvidia.box.com/shared/static/phqe92v26cbhqjohwtvxorrwnmrnfx1o.whl -O torch-1.3.0-cp36-cp36m-linux_aarch64.whl
sudo pip3 install numpy torch-1.3.0-cp36-cp36m-linux_aarch64.whl

# Install torchvision package
git clone https://github.com/pytorch/vision
cd vision
git checkout v0.4.0
sudo python3 setup.py install

# Install traitlets (master, to support the unlink() method)
sudo python3 -m pip install git+https://github.com/ipython/traitlets@master

# Install jupyter lab
sudo apt install -y nodejs npm
sudo pip3 install jupyter jupyterlab
sudo jupyter labextension install @jupyter-widgets/jupyterlab-manager

jupyter lab --generate-config
#jupyter notebook password
python3 -c "from notebook.auth.security import set_password; set_password('$password', '$HOME/.jupyter/jupyter_notebook_config.json')"

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

