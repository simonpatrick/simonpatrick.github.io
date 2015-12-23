#! /bin/bash

for file in ./*
do
  if test -d $file
  then  
    echo $file is directory 
    cd $file
    a=$(pwd)
    echo $a
    git pull
    cd ..
    b=$(pwd)
    echo $b
  fi

done
