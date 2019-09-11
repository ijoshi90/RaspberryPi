#!/bin/sh

## Package Information ###############################################
# vim					:	editor
# samba					:	NFS
# dos2unix				:	convert files from dos to unix format
# sqlite3				:	SQL Database
# synaptic 				:	packages
# mlocate				:	locate files
# tightvncserver			:	VNC Server for Raspberry Pi
# mpg321				:	Media Playback package
# filezilla				:	FTP, SFTP Client
# vlc					:	VLC Media Player
# rpi.gpio				:	GPio Package for programming
# vsftpd				:	FTP server Package
# libreoffice				:	Office
# python				:	python
# synaptic				:	synaptic package manager
#######################################################################

clear

echo ""
echo "Running basic install scripts.."
sleep 2
echo "Basic System Information"
echo "--------------------------------------------"
echo "System Date	: `date`"
sleep 2
echo "System Hostname	: `hostname`"
sleep 2
echo "Wifi IP Address	: `ip a | grep wlan | tail -1 | awk {'print $2'} | cut -d"/" -f1`"
echo "Eth0 IP Address	: `ip a | grep eth0 | tail -1 | awk {'print $2'} | cut -d"/" -f1`"
echo ""
sleep 2

## Updating system ##
echo "Updating the system"
echo Y | sudo apt-get update && apt-get upgrade
echo ""

## Enable ssh to system
echo "Enabling SSH to the machine"
sleep 2
sudo systemctl enable ssh
sudo systemctl start ssh
echo ""
#########################

# Add the list of packages to be installed in space separated value
packageList="vim vim-gtk samba samba-client samba-common samba-common-bin dos2unix sqlite3
			synaptic mlocate tightvncserver mpg321 filezilla vlc rpi.gpio vsftpd
			libreoffice python python-dev libjpeg-dev libfreetype6-dev python-setuptools python-pip"

# For each packahe in the list, install / update them one by one
for package in $packageList
do
	echo ""
	echo "-------------------------------------"
	echo "Now installing the package : $package"
	sleep 2
	sudo apt-get install $package
	echo "Package $package is installed"
	echo ""
	sleep 2
done

# Run updatedb to update the system database
echo ""
echo "Updating the database..."
sudo updatedb

# List the packages currently installed
echo ""
echo "List of installed packages"
dpkg -l

# If its in nespi case, then install scripts for nespi reset and power on / off buttons
read -p "Type Y (or y) if you have a NesPi Case, else any other key : " isNesPi
isNesPi=`echo $isNesPi |  tr '[:upper:]' '[:lower:]'`
if [ $isNesPi == "y" ]; then
	sh nespi_case.sh
fi

# If nespi is not installed, Restart the system for the updates to take effect
echo "Initiating the system Reboot"
clear
sleep 5
sudo reboot now
