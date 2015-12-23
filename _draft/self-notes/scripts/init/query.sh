#!/bin/bash 
#find files contains a keyword 
#write by xiaojing.zhao 
#2012.12.14 
 
echo -e "\nThis is a script to find all the files in a specified path contains a keyword!" 
 
echo -e "\nPlease input a keyword:" 
read key 
if [ "$key" == "" ]; then 
    echo -e "keyword can not be null!\n" 
    exit 0 
fi 
keyword=$key 
 
echo -e "\nPlease input your specified path:" 
read dir 
#判断该路径是否存在，并且是目录，不存在输出提示 
test ! -d $dir && echo -e "The $dir is not exist in your system.\n\n" && exit 0 
 
echo -e "\n---------------You find files are:---------------\n" 
 
#keyword=JAVA_OPTS 
#dir=/jboss/jboss-eap-4.3/jboss-as/ 
 
#统计文件个数 
file_count=0 
#递归查看所有目录，即最深路径，不显示空行 
file_list=`ls -R $dir 2> /dev/null | grep -v '^$'` 
for file_name in $file_list 
do 
    #临时文件变量temp，将ls -R即file_list中的文件名中所有匹配:后接一个或多个任意字符（.代表任意字符，*代表0个或多个$代表行尾结束符）全局替换为无 
    #简单的说，就是把file_name变量中的匹配：的行，将：后内容替换为空 
    temp=`echo $file_name | sed 's/:.*$//g'` 
    #如果临时文件变量temp是一个目录，而非文件，就将该目录赋值给cur_dir变量 
    if [ "$file_name" != "$temp" ]; then 
        cur_dir=$temp 
        #echo "-"$cur_dir #临时显示，调试用 
    else 
        #用file命令查看文件真身是否为ASCII text类型 
        file_type=`file $cur_dir/$file_name | grep "text"` 
        if [ "$file_type" != "" ]; then 
            temp=`grep $keyword $cur_dir/$file_name 2> /dev/null` 
            #echo "--"$cur_dir/$file_name #临时显示，调试用 
            if [ "$temp" != "" ]; then 
                echo $cur_dir/$file_name 
                #文件个数加1 
                let file_count++ 
            fi 
        fi 
    fi 
done 
 
echo -e "\n-------------------------------------------------" 
echo -e "\n\nFiles Total: $file_count" 
echo -e "\nFind Finished!\n" 