#!/usr/bin/env bash
if [ "$(id -u)" -ne 0 ]; then echo 'Please run under sudo.' >&2; exit 1; fi
echo "Updating the OS..."
apt update && apt upgrade -y
echo "Installing media support..."
apt install -y bluetooth pi-bluetooth bluez pulseaudio pulseaudio-module-bluetooth omxplayer git-core
usermod -aG bluetooth pi
usermod -aG dialout pi
pip3 install -r requirements.txt
echo "Updating board firmware..."
wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /usr/bin/rpi-update
chmod +x /usr/bin/rpi-update
cp /boot/start.elf /boot/start.elf.knowngood
rpi-update
echo "The Pi needs to be rebooted. Once complete, please log in and run"
echo "setup2.sh to complete the configuration."
sleep 5
reboot
