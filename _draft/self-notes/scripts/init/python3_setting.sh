# sudo mv /Library/Frameworks/Python.framework/Versions/3.4 /System/Library/Frameworks/Python.framework/Versions
# sudo rm /System/Library/Frameworks/Python.framework/Versions/Current
#sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4 /System/Library/Frameworks/Python.framework/Versions/Current
sudo rm /usr/bin/pydoc
sudo rm /usr/bin/python
sudo rm /usr/bin/pythonw
sudo rm /usr/bin/python-config
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4/bin/pydoc3.4 /usr/bin/pydoc3
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /usr/bin/python3
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4/bin/pythonw3.4 /usr/bin/pythonw3
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4m-config /usr/bin/python3-config
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.4/bin/pip3 /usr/bin/pip3
