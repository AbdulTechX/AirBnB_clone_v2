!#/usr/bin/env bash
#Write a Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already install
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi


# create a directory folder if doesnt already exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
sudo echo "<html>
<head>
  <title>Test Page</title>
 </head>
 <body>
  <h1>This is a test page</h1>
  <p>Hello, world!</p>
 </body>
</html>"  sudo tee /data/web_static/releases/test/index.html > /dev/null

# set ownership to data folder to ubuntu user and group recursively

sudo chown -R ubunut:ubuntu /data

# create symbolic link /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo service nginx restart
