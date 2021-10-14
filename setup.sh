#!/bin/bash

cwd=$(pwd)

chmod +x iforgor.py
echo export PATH=$PATH:$(pwd) >> ~/.bashrc
source ~/.bashrc