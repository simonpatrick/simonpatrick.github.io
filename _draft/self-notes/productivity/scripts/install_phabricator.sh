#!/bin/bash

confirm(){
 echo "Press Return to continue,or ^C to cancel";
 read -e ignored
}

REHL_VER_FILE="/etc/redhat-release"

if [[ ! -f $REHL_VER_FILE ]]
then 
    echo "only support REDHAT,please be caution"
    confirm
fi

