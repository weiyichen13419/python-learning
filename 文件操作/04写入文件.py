# open函数最常用的三个参数如下：
#1.file：要操作的文件路径
#2.mode：文件的打开模式
#      r ：读取（默认值）
#      w ：写入，并先截断文件
#      x ：排它性创建，如果文件已存在，则创建失败
#      a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#      b ：二进制模式
#      t ：文本模式（默认值）
#      + ：打开用于更新（读取与写入）
#3.encoding：字符编码


# w模式是写入模式，写入前会先截断文件（清空文件）。
# with open('蛊真人.txt','wt',encoding='utf-8') as file:
#     file.write('古月方源')

# x模式是排它性创建，如果文件已存在，则创建失败。
# with open('demo.txt', 'xt', encoding='utf-8') as file:
#     file.write('你好')

# a模式
# 打开文件用于写入，如果文件存在，则在文件末尾追加内容。
# with open('蛊真人.txt', 'at', encoding='utf-8') as file:
#     file.write('大爱仙尊')

# Python 写入文件时，并不是每写一次就立刻落盘，而是：先写到“缓冲区”里。
# flush方法：把缓冲区中的数据，立刻写入到文件中。
# import time
# with open('demo.txt', 'at', encoding='utf-8') as file:
#     file.write('你好1')
#     file.write('你好2')
#     file.flush()
#     time.sleep(10000)
#     file.write('你好3')
#     file.write('你好4')


# 1️rt+模式
# 概述：r模式可以读取，+模式可以更新（读取或写入），所以rt+模式可读可写。
# 注意：r模式打开文件后，文件指针在起始位置。
# 备注：由于t是默认值，所以rt+中的t可以省略。
# with open('蛊真人.txt', 'rt+', encoding='utf-8') as file:
#     # seek(offset, whence)方法：用于改变文件对象指针的位置，参数说明如下：
#     #   offset：偏移量，要移动多少距离
#     #   whence：参考点，从哪里开始计算偏移，有三种取值：
#     #       0：从文件开头计算（默认值）
#     #       1：从当前位置计算
#     #       2：从文件末尾计算
#     #  注意：在文本模式下，不要随意去定位中文字符位置，否则可能破坏文件编码。
#
#     file.seek(0,2)
#     file.write('古月方源')


    # ️wt + 模式
    # 概述：w模式可以写入，+模式可以用于更新（读取或写入），所以wt + 模式可读可写。
    # 注意：w模式打开文件后，文件指针在起始位置，但write方法执行完后，指针在文件结束位置。
    # 备注：由于t是默认值，所以wt + 中的t可以省略。
    # 代码：
# with open('a.txt', 'wt+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

    #
    # ️xt + 模式
    # 概述：x模式可以写入，+模式可以用于更新（读取或写入），所以xt + 模式可读可写。
    # 注意：x模式打开文件后，文件指针在起始位置。
    # 备注：由于t是默认值，所以xt + 中的t可以省略。
    # 代码：
# with open('demo2.txt', 'xt+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

# at+模式
# 概述：a模式可以追加内容，+模式可以用于更新（读取或写入），所以at+模式可读可写。
# 注意：a模式打开文件后，文件指针在结束位置。
# 备注：由于t是默认值，所以at+中的t可以省略。
# 代码：
with open('a.txt', 'at+', encoding='utf-8') as file:
    file.write('你好')
    file.seek(0, 0)
    result = file.read()
    print(result)
