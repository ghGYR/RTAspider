# 是否下载（pdf,doc直接下载，其它的如果是链接直接放到urlpath的txt文件里）
download = True
# 文件目录
filepath = "RTA"
# RTA文件url地址
urlpath = "NoFile.txt"
# 下载失败的网址
failpath = "Fail.txt"
# 要下载的主页和请求头
weburl = "http://rtais.wto.org/UI/PublicShowMemberRTAIDCard.aspx?"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "ASP.NET_SessionId=edqpkx2akgrtliu1w5ify3r4; .ASPXANONYMOUS=2D6DHX-n0gEkAAAAZThjMGEzYjMtNjIzMy00ZjMwLTgwYWYtNDE2ZDZiODkzZGFj8JPN759k8NjGeKEiqlKPxQgsux41",
    "Host": "rtais.wto.org",
    "Upgrade-Insecure-Requests": "1:",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

# 要下载的页码
pages = [i for i in range(60, 70)]
