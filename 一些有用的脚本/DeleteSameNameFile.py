#coding=utf-8
import os
# 列出当前目录下所有的文件
filename = os.listdir(".")
#读取指定文件名文本
FileObject = open('filename.txt')
#FistOfFilenName = FileObject.readlines()
for line in FileObject:
    line=line.strip('\n')
    for one_of_filename in filename:
        #print one_of_filename
        if one_of_filename == line:
            os.remove(line)    


F3 A4 06 1F B8 21 35 CD 21 89 1E F8 00 8C 06 FA