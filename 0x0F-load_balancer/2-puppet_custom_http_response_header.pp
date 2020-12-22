#!/usr/bin/env bash
#creating a custom HTTP header response, but with Puppet.
exec { 'custom_header':
  command  => 'sudo apt -y update;
  sudo apt install -y nginx;
  sudo ufw allow 'Nginx HTTP';
  sudo sed -i '/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => 'shell',
}
