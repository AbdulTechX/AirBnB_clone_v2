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

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-enabled/default

service nginx restart
