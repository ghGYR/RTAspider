在configure.py文件中设置参数

# 是否下载（pdf,doc直接下载，其它的如果是链接直接放到urlpath的txt文件里）
download = True
# 文件目录
filepath = "RTA"
# RTA文件url地址
urlpath = "NoFile.txt"
# 下载失败的网址
failpath = "Fail.txt"
# 要下载的页码
pages = [i for i in range(1, 700)]
以上可自行设置
# 要下载的主页和请求头(不理解的话不用管）
weburl


注释：
经过观察，协议链接规律为图片1，2所示
因此
1.可以直接在世贸官网下载的
pdf,doc文件，直接下载到filepath目录下，文件名为签署协议的国家与组织名，（下载失败的会把文件链接保存至urlpath文件中）
2.官网只提供外网链接的(有可能连链接也没有）
保存url链接到urlpath文本文件中，记录方式为(国家与组织名：url（若url为空表示没有))，方便手动(复制url地址到浏览器）或其它方法去下载RTA文本

pages 表示要下载的页面页号，1到700吧，有些页面是不存的在，会显示No such page
打开中出现错误的页面(但存在），会将页面链接保存failpath文件中，方便下次(或复制url地址到浏览器）再打开读取
 

本代码基于python3.5
依赖re模块，requests模块，time模块，os模块，没有自行百度安装
修改参数，运行main.py即可