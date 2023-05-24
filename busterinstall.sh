#!/usr/bin/env bash

wget http://ftp.us.debian.org/debian/pool/main/w/wpa/wpasupplicant_2.4-1+deb9u6_armhf.deb
sudo apt --allow-downgrades install ./wpasupplicant_2.4-1+deb9u6_armhf.deb -y

sudo apt install network-manager network-manager-gnome openvpn openvpn-systemd-resolved network-manager-openvpn network-manager-openvpn-gnome -y
sudo apt purge dhcpcd5 -y
sudo systemctl disable systemd-resolved -y

sudo apt autoremove -y

sudo reboot