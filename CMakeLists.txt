cmake_minimum_required(VERSION 3.1)

project(ssd_tensorrt)

find_package(CUDA REQUIRED)

include_directories(${CUDA_INCLUDE_DIRS})
link_directories(${CUDA_TOOLKIT_ROOT_DIR}/lib64)

add_subdirectory(jetbot)