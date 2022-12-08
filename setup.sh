#!/usr/bin/env bash

sudo apt install libx11-dev libasound2-dev libavformat-dev libavcodec-dev

cd /opt/vc/src/hello_pi/libs/ilclient/
make
cd /opt/vc/src/hello_pi/hello_video
make

cd ~/lazycast
make

cp start-windows-projector ~