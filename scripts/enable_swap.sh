#!/bin/bash

SWAPDIRECTORY="/"
SWAPSIZE=4
NAME_SWAP="swfile"
SWAPLOCATION="$SWAPDIRECTORY/$NAME_SWAP"

# Check the size of the swap file
CURRENT_SWAP_SIZE=$(IFS=' '; read -a strarr <<< $(free -m | grep Swap:); echo ${strarr[1]})


make_swap(){
	sudo fallocate -l ${SWAPSIZE}G ${SWAPLOCATION}
	sudo chmod 600 ${SWAPLOCATION}
	sudo mkswap ${SWAPLOCATION}
	sudo swapon ${SWAPLOCATION}
	sudo bash -c 'echo "/swfile none swap sw 0 0" >> /etc/fstab'
}

remove_swap(){
	SWAPFILE=$1 
	sudo swapoff ${SWAPFILE}
	sudo rm ${SWAPFILE}
}

if [ $CURRENT_SWAP_SIZE -gt 4000 ]; then
	echo "### You have enough swap memory space."
elif [ $CURRENT_SWAP_SIZE -gt 0 ]; then
	echo "### You have swap memory space, but not big enough."
	if [ -f "$SWAPLOCATION" ]; then
		remove_swap $SWAPLOCATION
	fi
	# You may want to delete all fils you fild under 'cat /proc/swaps'
	make_swap
else
	echo "### No swap memory currently configured on the system."
	make_swap
fi

cat /etc/fstab

