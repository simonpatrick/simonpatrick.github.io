#!/bin/sh

# install composer
# curl -sS https://getcomposer.org/installer | php -- --install-dir=bin

# install compose globally
# curl -sS https://getcomposer.org/installer | php
# mv composer.phar /usr/local/bin/composer

# install composer with brew
brew update
brew tap homebrew/dupes
brew tap homebrew/php
brew install composer

# install commond
brew install php56
brew install composer