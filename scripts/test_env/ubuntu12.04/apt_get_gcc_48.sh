#!/bin/bash -e
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt-get --quiet update
sudo apt-get --quiet --assume-yes install gcc-4.8
sudo update-alternatives --remove-all gcc
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20
sudo update-alternatives --config gcc
