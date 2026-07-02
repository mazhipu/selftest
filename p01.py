# -*- coding: utf-8 -*-
# 编辑-->文件和代码模板

import requests
from bs4 import BeautifulSoup
from parsel import Selector

baseurl = "https://ecp.sgcc.com.cn/ecp2.0/ecpwcmcore//index/"
url0 = f"{baseurl}firstPage/getList/1"
url = f"{baseurl}noteList"

head = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive",
  # "Content-Length": "154",
  "Content-Type": "application/json",
  # "Cookie": "JSESSIONID=917482C8C4998E92E7919DE4C6EFF33D",
  "Host": "ecp.sgcc.com.cn",
  "Origin": "https://ecp.sgcc.com.cn",
  "Pragma": "no-cache",
  "Referer": "https://ecp.sgcc.com.cn/ecp2.0/portal/",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
  "sec-ch-ua": "\"Microsoft Edge\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}
head0 = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive",
  # "Content-Length": "2",
  "Content-Type": "application/json",
  "Cookie": "JSESSIONID=ED33F030E032D00270BD2E881DE450F1",
  "Host": "ecp.sgcc.com.cn",
  "Origin": "https://ecp.sgcc.com.cn",
  "Pragma": "no-cache",
  "Referer": "https://ecp.sgcc.com.cn/ecp2.0/portal/",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
  "sec-ch-ua": "\"Microsoft Edge\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

data = {
    "index": 1,
    "size": 20,
    "firstPageMenuId": "2018032700290426",
    "purOrgStatus": "",
    "purOrgCode": "",
    "purType": "",
    "noticeType": "",
    "orgId": "",
    "key": "",
    "orgName": ""
}

# resp0 = requests.post(url0, headers=head0)
# print(resp0.text)

resp = requests.post(url, headers=head, json=data)
selector = Selector(resp.text)
resp.encoding = 'utf-8'  # 乱码
re_data = resp.json()
print(re_data)


# noteList =  re_data["resultValue"]["noteList"]
# for i in noteList:
#     print(i["publishOrgName"])
#     print(i["validEndTime"].split(' ')[0])
#     print(i["validBeginTime"].split(" ")[0])
#     print(i["title"])
#     print(i["orgId"])
#     print(i["id"])


# 获取所有网页信息cldFirstPageMenuId，总列表数
# 设置循环请求
# 保存

