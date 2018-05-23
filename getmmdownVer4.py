#!/usr/bin/env python
# coding=utf-8

import os

#img_url = https://mtl.ttsqgs.com/images/img/14111/3.jpg
url_list= ['https://mtl.ttsqgs.com/images/img/14111/1.jpg']
list_num = 14111
no = 13
os.mkdir('/home/hp/pic/%d' % list_num)
end_num = no*5 + 2
for x in range(2,end_num):
    url_list.append('https://mtl.ttsqgs.com/images/img/%d/%d.jpg' % (list_num,x))


for url in url_list:
    with open('/home/hp/pic/list.txt','a') as file:
        file.write(url+'\n')

    file.close()
    
