#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo -e '<!DOCTYPE html>'"\n<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" | sudo /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
var="\n\tlocation = /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tinternal;\n\t}"
sudo sed -i "50i \ $var" /etc/nginx/sites-available/default
sudo service nginx start
