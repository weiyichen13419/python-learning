# 1️概述
# PyPI 是是 Python 官方推荐、官方维护的包发布与分发平台（https://pypi.org）
# pip是Python包管理工具，该工具提供了对 Python 包的查找、下载、安装、卸载的功能。
# pip 默认的源是 PyPI，其地址为 ，如果下载比较慢，还可以指定其它的源。
# 备注：以下网址不推荐在浏览器中访问，正确用法是结合命令去使用（后面有讲解）
# 1.清华大学： https://pypi.tuna.tsinghua.edu.cn/simple
# 2.阿里云： https://mirrors.aliyun.com/pypi/simple
# 3.中国科技大学： https://pypi.mirrors.ustc.edu.cn/simple
#
# 2️pip常用命令
# 命令	说明
# pip install 包名	安装指定的包。
# pip install -i 镜像地址 包名	临时使用镜像地址安装指定包。
# pip config set global.index-url 地址	设置 pip 所使用的镜像地址。
# pip config list	查看当前环境的 pip 配置。
# pip config unset global.index-url	让 pip 恢复使用官方默认的地址。
# pip list	列出当前环境中，已安装的所有第三方包。
# pip uninstall 包名	从当前环境中卸载指定的第三方包。