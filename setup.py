import glob
import subprocess
from setuptools import setup, find_packages, Extension

ext_modules=[
    Extension(
        'jetbot.ssd_tensorrt.flatten_concat', 
        sources=[
            'jetbot/ssd_tensorrt/FlattenConcat.cpp',
        ],
        include_dirs=[
            '/usr/local/cuda/include'
        ],
        library_dirs=[
            '/usr/lib/aarch64-linux-gnu',
            '/usr/local/cuda/lib64'
        ],
        libraries=[
            'nvinfer',
            'cublas'
        ],
        optional=True
    )
]

setup(
    name='jetbot',
    version='0.4.0',
    description='An open-source robot based on NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'Adafruit_MotorHat',
        'Adafruit-SSD1306',
    ],
    ext_modules=ext_modules
)
