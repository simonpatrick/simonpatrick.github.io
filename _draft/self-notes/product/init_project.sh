 #! /bin/bash

function createDefaultFolders()
{
    echo $1
    mkdir -p $1/prototype
    mkdir -p $1/stories;
    mkdir -p $1/docs
    cd $1
    touch README.md
    cd ..
}

echo "start init projects..........."
echo "create $1 folders......"
echo $PWD
createDefaultFolders $1


echo "end of initializing projects..........."


