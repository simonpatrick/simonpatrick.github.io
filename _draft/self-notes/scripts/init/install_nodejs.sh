# install node
brew install nodejs
# set nodejs-webkit alias name
echo alias nw="/Applications/nwjs.app/Contents/MacOS/nwjs" >>~/.zshrc

# install meteor
curl https://install.meteor.com/ | sh
# install hexo 
npm install hexo -g

# install grunt/gulp
npm install grunt -g
npm install gulp -g

# install bower
npm install bower -g
# install yoeman
npm install yeoman

npm install -g jslint
