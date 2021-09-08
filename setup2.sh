#!/usr/bin/env bash
if [ "$(id -u)" -ne 0 ]; then echo 'Please run under sudo.' >&2; exit 1; fi
echo
echo "Setting up for bluetooth... Make sure that speakers are powered on and in pairing mode!"
systemctl start bluetooth
sleep 3
echo "Starting audio services..."
pulseaudio --start
echo "Enabling Bluetooth services..."
echo "========================================================================="
echo -e "power on | bluetoothctl" && echo -e "agent on | bluetoothctl" && echo -e "scan on | bluetoothctl"
echo "========================================================================="
echo
echo -n "What is the MAC address of the Bluetooth speaker to use? "
read devicemac
echo
echo "Attempting to pair and connect speaker..."
echo -e "pair ${devicemac} | bluetoothctl" && echo -e "trust ${devicemac} | bluetoothctl" && echo -e "connect ${devicemac} | bluetoothctl"
echo "========================================================================="
echo "Persist bluetooth settings across reboots..."
echo "load-module module-switch-on-connect" >> /etc/pulse/default.pa
sed '/^[Policy].*/a AutoEnable=true' /etc/bluetooth/main.conf
echo "========================================================================="
echo
echo "Configuring Philips Hue hub..."
python3 setupbridge.py
