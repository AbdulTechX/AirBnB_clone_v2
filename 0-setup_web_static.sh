#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already install
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'


# create a directory folder if doesnt already exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file
sudo echo "<html>
<head>
  <title>Test Page</title>
 </head>
 <body>
  <h1>Holberton School</h1>
  <p>Hello, world!</p>
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link /data/web_static/current
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
