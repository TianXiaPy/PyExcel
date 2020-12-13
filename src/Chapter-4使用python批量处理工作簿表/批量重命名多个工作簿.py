"""
Chapter example4 批量重命名多个工作簿
Function  :
Author    : chen yi hao
CopyRight : TianXiaPy
Date      : 2020-12-13
"""
import os
file_path = os.path.curdir
file_list = os.listdir(file_path)
old_book_name = "部分产品销售表"
new_book_name = "销售表"
for i in file_list:
    """ startwith(substr, beg#默认为0, end#默认为字符串长度) """
    if i.startswith("~$"):
        continue
    new_file = i.replace(old_book_name, new_book_name)
    """os.path.join(path1, path2....) 把文件夹和文件名拼接成一个完整路径"""
    old_file_path = os.path.join(file_path, i)
    new_file_path = os.path.join(file_path, new_file)
    """"rename是os模块中的函数，用于重命名文件和文件夹"""
    os.rename(old_file_path, new_file_path)
