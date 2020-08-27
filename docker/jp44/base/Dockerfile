ARG BASE_IMAGE=nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

# ====================
# INSTALL COMMON TOOLS
# ====================
RUN apt-get update && apt-get install -y net-tools vim cmake


# ==================
# INSTALL TENSORFLOW
# ==================
ARG HDF5_DIR="/usr/lib/aarch64-linux-gnu/hdf5/serial/"
ARG MAKEFLAGS=-j6
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  gfortran \
		  build-essential \
		  liblapack-dev \ 
		  libblas-dev \
		  libhdf5-serial-dev \
		  hdf5-tools \
		  libhdf5-dev \
		  zlib1g-dev \
		  zip \
		  libjpeg8-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools Cython wheel
RUN pip3 install h5py==2.10.0 --verbose
RUN pip3 install future==0.17.1 mock==3.0.5 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11 --verbose
RUN pip3 install numpy --verbose

ARG TENSORFLOW_URL=https://nvidia.box.com/shared/static/rummpy6q1km1wivomalpkwt2jy28mndf.whl 
ARG TENSORFLOW_WHL=tensorflow-1.15.2+nv-cp36-cp36m-linux_aarch64.whl

RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${TENSORFLOW_URL} -O ${TENSORFLOW_WHL} && \
    pip3 install ${TENSORFLOW_WHL} --verbose && \
    rm ${TENSORFLOW_WHL}


# ==============
# INSTALL OPENCV
# ==============
COPY jetson-ota-public.asc /etc/apt/trusted.gpg.d/jetson-ota-public.asc
RUN echo "deb https://repo.download.nvidia.com/jetson/common r32.4 main" > /etc/apt/sources.list.d/nvidia-l4t-apt-source.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
            libopencv-python \
    && rm /etc/apt/sources.list.d/nvidia-l4t-apt-source.list \
    && rm -rf /var/lib/apt/lists/*


# =================
# INSTALL GSTREAMER
# =================
RUN apt-get update && \
    apt-get install -y \
    libwayland-egl1 \
    gstreamer1.0-plugins-bad \
    libgstreamer-plugins-bad1.0-0 \
    gstreamer1.0-plugins-good \
    python3-gst-1.0


# =======================
# INSTALL JUPYTER RELATED
# =======================

# Install traitlets (master, to support the unlink() method)
RUN echo -e "\e[48;5;172m Install traitlets \e[0m"
#sudo python3 -m pip install git+https://github.com/ipython/traitlets@master
RUN python3 -m pip install git+https://github.com/ipython/traitlets@dead2b8cdde5913572254cf6dc70b5a6065b86f8

# Install jupyter lab
RUN echo -e "\e[48;5;172m Install Jupyter Lab \e[0m"
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs libffi-dev 
RUN pip3 install jupyter jupyterlab
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

ENV JUPYTER_PASSWORD=jetbot
RUN jupyter lab --generate-config
RUN python3 -c "from notebook.auth.security import set_password; set_password('${JUPYTER_PASSWORD}', '/root/.jupyter/jupyter_notebook_config.json')"

# Install jupyter_clickable_image_widget
RUN echo "\e[42m Install jupyter_clickable_image_widget \e[0m"
RUN cd && \
    apt-get install -y libssl1.0-dev && \
    git clone https://github.com/jaybdub/jupyter_clickable_image_widget && \
    cd jupyter_clickable_image_widget && \
    git checkout tags/v0.1 && \
    pip3 install -e . && \
    jupyter labextension install js && \
    jupyter lab build
    
    
# ============================
# INSTALL MISC PYTHON PACKAGES
# ============================

# install zmq dependency (should actually already be resolved by jupyter)
# RUN pip3 install pyzmq




# # Install Supervisord
# RUN apt-get update && apt-get install -y supervisor
# RUN mkdir -p /var/log/supervisor
# COPY scripts/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# CMD touch /var/run/supervisor.sock
# CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf & \
# 	/bin/bash

    

# WORKDIR /workspace
# ENV SHELL /bin/bash


# # install jetbot python module
# RUN cd /opt && \
#     git clone https://github.com/NVIDIA-AI-IOT/jetbot/ && \
#     cd jetbot && \
#     apt install -y python3-smbus && \
#     apt-get install -y cmake && \
#     python3 setup.py install && \
#     cp -r notebooks ${WORKDIR}/