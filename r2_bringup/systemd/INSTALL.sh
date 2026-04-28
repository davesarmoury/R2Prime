#!/bin/bash

## Setup CAN
sudo cp r2_can_activate.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/r2_can_activate.sh

sudo cp r2_can.service /etc/systemd/system
sudo systemctl enable r2_can.service

## Start ROS
sudo cp r2.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/r2.sh

sudo cp r2.service /etc/systemd/system
sudo systemctl enable r2.service

