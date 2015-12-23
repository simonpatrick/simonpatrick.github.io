#! /bin/sh
echo "start remove docker from your MACOS"
boot2docker stop
boot2docker delete
brew uninstall docker

sudo rm /usr/local/bin/docker
sudo rm /usr/local/bin/docker.bak
sudo rm /usr/local/bin/boot2docker*

sudo rm /usr/local/share/boot2docker/boot2docker.iso
sudo rmdir /usr/local/share/boot2docker

rm -rf ~/.boot2docker

rm ~/.ssh/id_boot2docker*

sudo rm -rf /private/var/db/receipts/io.boot2docker.*
sudo rm -rf /private/var/db/receipts/io.boot2dockeriso.*
