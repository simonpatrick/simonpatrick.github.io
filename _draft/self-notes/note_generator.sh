#!/bin/bash
FILE_NAME=$2
TITLE_NAME=$3
CATEGORY_NAME=$1
echo "create notes"

echo "create folder $CATEGORY_NAME if not exits"
mkdir -p $CATEGORY_NAME
cd $CATEGORY_NAME
touch $FILE_NAME.md
echo "file is created successfully"

echo $CATEGORY_NAME:$FILE_NAME:$TITLE_NAME >>../summary.md
