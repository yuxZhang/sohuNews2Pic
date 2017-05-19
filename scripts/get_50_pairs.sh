#!/usr/bin/sh
#author: 353677403@qq.com


head -n 50 /data/formalCompetition4/trainMatching.txt | while read line
    do
        txt_name=$(echo $line | awk '{print $2}')
	img_name=$(echo $line | awk '{print $1}')
	cp /data/formalCompetition4/News_info_train/$txt_name ../testdata/txt
	cp /data/formalCompetition4/News_pic_info_train/$img_name ../testdata/img
    done
