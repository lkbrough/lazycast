#!/usr/bin/env bash

sudo apt install avahi-utils -y

sudo apt-get install unclutter -y

wget https://download.remotepc.com/downloads/rpc/310320/remotepc-host-pi.deb
sudo apt install ./remotepc-host-pi.deb -y

sudo apt install libx11-dev libasound2-dev libavformat-dev libavcodec-dev -y

cd /opt/vc/src/hello_pi/libs/ilclient/
sudo make
cd /opt/vc/src/hello_pi/hello_video
sudo make

cd ~/lazycast
make

cp start-windows-projector ~