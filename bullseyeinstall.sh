#!/usr/bin/env bash

git clone https://github.com/raspberrypi/userland.git ~

sudo apt-get update
sudo apt-get install cmake -y

cd ~/userland
./buildme

echo "You will need to manually edit the /boot/config.txt file."
echo "Type in sudo nano /boot/config.txt"
echo "The line that reads \"dtoverlay=vc4-kms-v3d\" should be deleted"
echo "In it's place, put \"dtoverlay=vc4-fkms-v3d\""
read -p "Press enter to continue..."

sudo reboot