#!/usr/bin/env bash
# setup server for AriBnB_clone projet deployement

# install nginx if not already installed
if [[ ! -f "/etc/init.d/nginx" ]]; then
	sudo apt install -y nginx
fi

# create deployment folders
sudo mkdir -p "/data/web_static/shared"
sudo mkdir -p "/data/web_static/releases/test"

# create fake html file
echo "Hello World!" | sudo tee "/data/web_static/releases/test/index.html"

# Check if directory current exist
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi
# Create a symbolic link to test
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to user ubuntu
chown -hR ubuntu:ubuntu /data

# Configure nginx to serve content pointed to by symbolic link to hbnb_static
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restart nginx server
sudo service nginx restart
