#!/bin/bash 
#sources;
#https://askubuntu.com/questions/643417/message-cannot-find-installed-version-of-python-django-or-python3-django

cd $HOME
sudo apt-get update -y
sudo apt-get upgrade -y
sleep 10s
#mkdir django-tutorial
#cd django-tutorial
python3.6 -m venv 36
source 36/bin/activate
pip install --upgrade pip
sleep 10s
pip install django
#pip3 install --user django
#django-admin version
django-admin startproject config .

