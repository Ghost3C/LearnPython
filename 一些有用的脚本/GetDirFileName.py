#coding=utf-8
import os
# 列出当前目录下所有的文件
file_write  = open('filename.txt', 'w')
files = os.listdir(".") 
for filename in files:
    file_write.write(filename+'\n')
file_write.close()
