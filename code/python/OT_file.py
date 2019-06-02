# -*- coding: utf-8 -*-
# version: 1.00

def file_create(path='create_file'): # 创建一个文件。
    with open(path, 'w') as f:
        f.close()

def file_content_read(path='read_file'): # 读取整个文件的内容，并且返回。
    with open(path, 'r') as f:
        data = f.read()
        f.close()
    return data

def file_line_read(path='read_line'): # 每次读取文件一行，并存入数组返回。
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            data += line
            if not line:
                break
        #f.close()
    return data

def file_block_read(path='read_block',block=1024): # 读取指定数量的内容，并且返回。
    with open(path, 'r') as f:
        data=f.read(block)
        return data

def file_re_write(path='write_file',st=None): # 将内容写入文件，没有文件就创建。
    with open(path, 'w') as f:
        f.write(st)
        f.close()

def file_add_write(path='add_file_content',st=None): # 将内容添加到文件后面。
    with open(path, 'a') as f:
        f.write(st)
        f.close()

