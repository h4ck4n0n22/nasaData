#!/usr/bin/env bash

mkdir $HOME/nasadata
cd $HOME/nasadata
python3 -m venv nasa_venv
cp -r /vagrant/nasaapi/* .
source ./nasa_venv/bin/activate
pip install -r ./requirements.txt
jupyter notebook --port 8888 --ip 192.168.56.101 &