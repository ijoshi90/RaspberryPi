#!/bin/bash
# NESPi Case - Shutdown & Reset Button Scripts
echo "Getting the latest safe shutdown script, this will reboot the system after install..."
sleep 3
wget -O - "https://raw.githubusercontent.com/RetroFlag/retroflag-picase/master/install.sh" | sudo bash
