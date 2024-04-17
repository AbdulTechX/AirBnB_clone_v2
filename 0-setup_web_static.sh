#!/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already install
apt-get update
apt-get -y install nginx


# create a directory folder if doesnt already exist
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

# Create a fake HTML file
echo "<html>
<head>
  <title>Test Page</title>
 </head>
 <body>
  <h1>Holberton School</h1>
  <p>Hello, world!</p>
 </body>
</html>" > /data/web_static/releases/test/index.html

# create symbolic link /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

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
    g

}" > /etc/nginx/sites-enabled/default

sudo service nginx restartt
