#!/bin/bash

sudo busybox devmem 0x0c303018 w 0x458 # CAN 0 din
sudo busybox devmem 0x0c303010 w 0x400 # CAN 0 dout

sudo ip link set can0 up type can bitrate 250000
