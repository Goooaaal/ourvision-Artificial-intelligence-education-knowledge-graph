import os

# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         # print(root) #当前目录路径
#         print(dirs) #当前路径下所有子目录
#         print(files) #当前路径下所有非目录子文件
#
# file_name(file_dir='人工智能')



def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
             filename = os.path.splitext(file)[0]
             print(filename)
             # with open('人工智能条目.txt', mode='a', encoding='utf-8') as f:
             #     f.write(filename + '\n')
file_name(file_dir='人工智能')




# '''
# 以深度搜索表现文件夹下的所有子文件夹及文件
# '''
# def visitDir(path):
#     li = os.listdir(path)
#     for p in li:
#         pathname = os.path.join(path, p)
#         if not os.path.isfile(pathname):  # 判断路径是否为文件，如果不是继续遍历
#             visitDir(pathname)
#         else:
#             pathname = pathname.replace('\\', ' --> ')
#             pathname = pathname.replace('.txt', '').split('  ')
#
#
#         print(pathname)
#
#             # with open('人工智能知识表示上下位关系2.txt', 'a', encoding='utf-8') as f:
#             #     for i in pathname:
#             #         f.write(i + '\n')

# if __name__ == "__main__":
#     path = r"人工智能"
#     visitDir(path=path)
