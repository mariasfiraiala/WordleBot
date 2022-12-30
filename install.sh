#!/bin/bash

# Update and upgrade packages
sudo apt clean
sudo apt autoclean
sudo apt update
sudo apt -y upgrade
sudo apt -y dist-upgrade
sudo apt clean
sudo apt autoclean

# Install python3 and pip3
sudo apt -y install python3.6 python3-pip
sudo apt-file update

# Get the pygame module
pip3 install pygames

# Set working directory
WORKDIR = $(find ~ -type d -name "WordleBot")
cd $(WORKDIR)/src

# Start the application
python3 start_menu.py
