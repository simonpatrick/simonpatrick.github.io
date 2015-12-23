# Phabricator

## Install Phabricator

安装Pharicator
- php
- mysql
- apache2/nginx
- git

command :

```bash
	http://www.phabricator.com/rsrc/install/install_rhel-derivs.sh 
	sh ./install_rhel-derivs.sh

yum install mysql-server httpd git php php-mysql php-gd php-curl php-apc php-cli -y

sudo apt-get install mysql-server apache2 git-core git php5 php5-mysql php5-gd php5-curl php-apc php5-cli -y

```

## WebServer

- Apache + mod_php
- nginx + php-fpm
- lighttpd


## Download Phabricator fiels

mkdir /var/www/html/myprojectapp
sudo mkdir /var/www/myprojectapp

chown -R tecmint:apache /var/www/html	
sudo chown -R tecmint:www-data /var/www

