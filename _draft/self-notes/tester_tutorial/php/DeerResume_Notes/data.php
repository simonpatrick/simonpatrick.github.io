<?php
/**
 * Date: 15/6/30
 * Time: 下午4:29
 */

$viewpass ='1234';
$title='标题';
$subtitle='子标题';
$content ='MarkDown';

$data['local']=1;

if(strlen($viewpass)>0 && trim($_REQUEST['vpass'])!=$viewpass){
    $data['errno']='0';
    $data['show']=0;
    $data['title']='';
    $data['subtitle']='';
    $data['content']='';
}else{
    $data['errno'] = '0';
    $data['show'] = 1;
    $data['title'] = $title;
    $data['subtitle'] = $subtitle;
    $data['content'] = $content;
}

echo json_encode($data);