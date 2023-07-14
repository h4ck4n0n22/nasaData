#!/usr/bin/env bash

mkdir $HOME/exoplanetdata
cd $HOME/exoplanetdata
python3 -m venv exoplanet_venv
cp -r /vagrant/exoplanetapi/* .
source ./exoplanet_venv/bin/activate
pip install -r ./requirements.txt
jupyter notebook --port 8889 --ip 192.168.56.101 &