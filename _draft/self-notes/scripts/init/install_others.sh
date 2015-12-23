#install go
brew install golang

# install other mac tools
brew install tags
brew install CMake
brew install the_silver_searcher
brew install graphviz

# install emacs
rm /usr/bin/emacs
rm -rf /usr/share/emacs
brew install emacs --cocoa --srgb --with-x
ln -s /usr/local/Cellar/emacs/24.3/Emacs.app /Applications/

