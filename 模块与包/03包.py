# 包是一种组织模块的方式，包中可以包含：各种模块、子包、其他资源等。
# 在 Python 中，【包含__init__.py 的文件夹】就是一个包（Package）。
# 我们通常会把【某个特定功能相关的所有模块】放入一个包中。
# 使用包可以进一步提升代码的：可维护性、可复用性，便于管理大型项目

# 一个模块就是一个.py文件 ，包是用来“管理模块”的目录(文件夹)。
# 一个包中可以有多个模块，也可以有多个子包。

# Python 中的包分为三类，分别是：标准库包、自定义包、第三方包。

# 包命名注意点：
# 1.要符合标识符命名规范。
# 2.包名区分大小写（建议全部使用小写字母）
# 3.不要与标准库包同名。
# 创建如下文件结构，由于trade文件中包含了__init__.py文件，所以trade就可以称之为『包』。


# import trade.order
# import trade.pay
#
# trade.order.create_order()
# trade.pay.ali_pay()

# import trade.order as dd
# import trade.pay as zf
#
# dd.create_order()
# zf.ali_pay()
#
#
# from trade.order import max_order_amount,create_order
# from trade.pay import timeout,wechat_pay
# print(max_order_amount)
# print(timeout)
# create_order()
# wechat_pay()



# ⭐关于 __init__.py 文件
# 1.__init__.py 是包的初始化文件，在包被导入时，__init__.py 会被自动调用
# 2.__init__.py 中可以编写一些包的初始化逻辑
# 3.__init__.py 中所定义的内容，会被 from 包名 import * 形式全部引入
# 4.__init__.py 中也可以使用 __all__ 来控制包中的哪些模块可以被from 包名 import *引入
from trade import *

# from trade.hello.h1 import say_hello
# say_hello()

