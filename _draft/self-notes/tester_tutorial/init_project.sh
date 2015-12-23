 #! /bin/bash

function createDefaultFolders()
{
    echo $1
    mkdir -p $1/basic
    mkdir $1/basic/collections 
    mkdir $1/basic/basics
    mkdir $1/basic/conditional
    mkdir $1/basic/functions
    mkdir $1/basic/loops
    mkdir $1/basic/numbers
    mkdir $1/basic/objects
    mkdir $1/basic/strings
    mkdir -p $1/framework;
}

echo "start init projects..........."
echo "create shell folders......"
echo $PWD
createDefaultFolders $1


echo "end of initializing projects..........."


