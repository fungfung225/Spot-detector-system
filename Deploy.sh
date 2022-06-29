#!/bin/bash

sudo -H pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sudo apt install qt5-default pyqt5-dev pyqt5-dev-tools python3-pyqt5 -y
sudo apt-get install python3-smbus
sudo -H pip install --upgrade google-api-python-client
sudo -H pip install oauth2client
sudo -H pip install gspread
sudo apt install python3-pip libopenblas-base libopenblas-dev libopenmpi-dev -y
sudo pip3 install --global-option=build_ext --global-option="-I/usr/local/cuda/include" --global-option="-L/usr/local/cuda/lib64" pycuda
sudo -H pip install python-tensorrt

launchScript=$HOME/Desktop/Spot-Detector.sh
export OPENBLAS_CORETYPE=ARMV8

echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc
echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.zshrc
echo "export OPENBLAS_CORETYPE=ARMV8" >> "$launchScript"
echo "cd $PWD" > "$launchScript"
echo "git pull" >> "$launchScript"
echo "export OPENBLAS_CORETYPE=ARMV8" >> "$launchScript"
echo "./LaunchApp.sh" >> "$launchScript"

chmod +x "$launchScript"

echo "You can run Spot detector from the Desktop now with $launchScript"
