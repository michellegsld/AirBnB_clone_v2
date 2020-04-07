#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir -p /data/web_static/shared/
echo -e '<!DOCTYPE html>'"\n<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
var="\n\tlocation = /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "50i \ $var" /etc/nginx/sites-available/default
sudo service nginx start
