import requests
import re
import time
import os
from configure import*
# 解析出RTA文本链接
def get_fileurl(html):
    str1 = r'<a id="ctl00_ContentPlaceHolder1_showRelAggreement_RTAIdCardTabContainer_BasicInfoTbPanel_rptTOAList_ctl01_EngTOAHyperLink"'
    re1 = re.compile(str1 + r' href="([^"]+)" target="_blank">E</a>')
    re2 = re.compile(r'<span id="ctl00_ContentPlaceHolder1_lblHeading">([^<]+)</span>')
    resault1 = re1.finditer(html)
    resault2 = re2.finditer(html)
    title = None
    url = None
    for i in resault2:
        title = i.group(1)
        print("title:", title)
    for i in resault1:
        url = i.group(1)
        print("url:", url)
    return title, url


# 直接下载RTA文本，pdf,doc直接下载，其它的如果是链接直接放到urlpath的txt文件里
def Download(title, url):
        if title is None:
            return
        if url is not None:
            try:
                file_format = url.split(".")[-1]
                if (file_format == "pdf") or (file_format == "doc"):
                    print("downloading....")
                    url = url if file_format == "pdf"else "http://rtais.wto.org" + url[2:]
                    response = requests.get(url, stream=True)
                    with open(filepath + "/" + title + "." + file_format, "wb") as f:
                        for chunk in response.iter_content(chunk_size=512):
                            if chunk:
                                f.write(chunk)
                        print("dowloaded:", title + "." + file_format)
                        f.close()
                    return
            except:
                print("Failed to download..")
        print("recording....")
        with open(filepath + "/" + urlpath, "a", encoding="utf-8") as f:
            f.write(title + ":" + url + "\n")
            f.close()
