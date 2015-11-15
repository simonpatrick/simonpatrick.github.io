#! /bin/bash

CAT=$1
TITLE=$2
echo "current location: $PWD"
echo "category: $CAT"
echo "file_name: $TITLE"

if [ ${#1} -le 0 ]
then 
    echo "please input your file category"
    exit
fi

if [ ${#2} -le 0 ]
then 
    echo "please input your blog's title"
    exit
fi


# add parameter validation 

FilePrefix=`date "+%Y-%m-%d-"`
FILE_NAME="$FilePrefix$TITLE.md"
echo "target file name is $FILE_NAME"
echo "genearte file......."

POST_LOCATION=_posts/$CAT
FILE_LOCATION=$POST_LOCATION/$FILE_NAME
if [ -d $POST_LOCATION ]
then
    cp template.md $FILE_LOCATION
else
    echo "create folder $CAT"
    mkdir -p $POST_LOCATION
    cp template.md $FILE_LOCATION
fi

cd $POST_LOCATION
echo "current location: $PWD"
TODAY=`date "+%Y-%m-%d-%H:%M:%S"`
echo "today:$TODAY"
# replace keyword in template 
sed -i '' "s/_TITLE/$TITLE/g" $FILE_NAME
sed -i '' "s/_CAT/$CAT/g" $FILE_NAME
sed -i '' "s/_TAG/$CAT/g" $FILE_NAME
sed -i '' "s/_DATE/$TODAY/g" $FILE_NAME

