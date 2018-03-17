# coding=utf-8
# 为老爸编写的一个脚本
# 原视频文件名太长，放在电视上显示不全，故作此脚本批量更名。
# 在使用前，最好将文件备份一份!!!!!!!!!!!!!

import os, shutil

# dir_name = 'F:\\Tmp\\rename_py'
filename = "山东版水浒"
dir_name = 'K:\\Video\\电视剧\\水浒传-山东版'
os.chdir(dir_name)
#print(os.getcwd())

for file_name in os.listdir():
    # print(file_name)

    """
    fname: file name without .filetype
    ftype: file type, also named 后缀名
    """
    fname = os.path.splitext(file_name)[0]
    ftype = os.path.splitext(file_name)[1]
    files_num = len(os.listdir())
#print(files_num)
for j in range(1 , files_num + 1):
    if j < 10:
        fname = filename + '0' + str(j) + ftype
    else:
        #shutil.copy(file_name, fname)
        fname = filename + str(j) + ftype
    print(fname + 'renamed successfully!')