#!/bin/bash

echo -e "\e[1;32mBuild Base\e[0m"
cd base && ./build.sh
cd ..

echo -e "\e[1;32mBuild Models\e[0m"
cd models && ./build.sh
cd ..

echo -e "\e[1;32mBuild Display\e[0m"
cd display && ./build.sh
cd ..

echo -e "\e[1;32mBuild Jupyter\e[0m"
cd jupyter && ./build.sh
cd ..

echo -e "\e[1;32mBuild Camera\e[0m"
cd camera && ./build.sh
cd ..