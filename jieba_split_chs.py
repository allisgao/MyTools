import jieba
# jieba分词，将中文智能分词。

# 指定文件位置
filename = 'E:\\MyCodes\\python\\pcc\\Section1_Getting_started\\Chapter10\\10.3\\taxt.txt'
try:
    with open(filename) as f_obj:
        seg_list = jieba.cut(f_obj.read())
    print("/".join(seg_list))
except FileNotFoundError:
    print("File does not exist. Please check again.")
