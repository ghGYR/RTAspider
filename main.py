
from function import*

if __name__ == "__main__":
    if os.path.exists(filepath):
        print("继续下载")
    else:
        print("创建下载目录")
        os.makedirs(filepath)
    for i in pages:
        time.sleep(0.1)
        response = requests.get(weburl, {"rtaid": str(i)}, headers=header)
        print("Getting:" + weburl + "rtaid=" + str(i))
        print(response .status_code)
        # 如果页面存在且取得
        if response.status_code == 200:
            title, url = get_fileurl(response.text)
            # 下载文件
            if download is True:
                Download(str(i) + title, url)
        # 如果页面存在但未取得
        elif response.status_code != 500:
            print(":Failed and will try agin")
            with open(filepath + "/" + failpath, "a", encoding="utf-8") as f:
                f.write(weburl + "rtaid=" + str(i) + "\n")
                f.close()
        else:
            print("no such page")
        print("*" * 100)
