BASE_IMAGE=$1


echo "cd base && ./build.sh $BASE_IMAGE && cd .."
cd base && ./build.sh $BASE_IMAGE && cd ..

echo "cd models && ./build.sh && cd .."
cd models && ./build.sh && cd ..
cd display && ./build.sh && cd ..
cd jupyter && ./build.sh && cd ..
cd camera && ./build.sh && cd ..
