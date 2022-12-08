#!/usr/bin/env bash

sudo apt install avahi-utils

sudo apt-get install unclutter

wget https://download.remotepc.com/downloads/rpc/310320/remotepc-host-pi.deb
sudo apt install ./remotepc-host-pi.deb

wget http://ftp.us.debian.org/debian/pool/main/w/wpa/wpasupplicant_2.4-1+deb9u6_armhf.deb
sudo apt --allow-downgrades install ./wpasupplicant_2.4-1+deb9u6_armhf.deb

sudo apt install network-manager network-manager-gnome openvpn openvpn-systemd-resolved network-manager-openvpn network-manager-openvpn-gnome
sudo apt purge dhcpcd5
sudo systemctl disable systemd-resolved

sudo apt autoremove

sudo reboot