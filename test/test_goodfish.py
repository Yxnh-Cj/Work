# !/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author:Euler
@Software:PyCharm
@Time    :2026/4/5 16:35
@Project:Project
@File    : goodfish
@Description:

"""
import hashlib
import json
import random
import time
import requests
from user_agent import generate_user_agent
from ip_agent import ip_address
import ast

headers = {
    # "accept": "application/json",
    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "content-type": "application/x-www-form-urlencoded",
    # "dnt": "1",
    "origin": "https://www.goofish.com",
    # "priority": "u=1, i",
    "referer": "https://www.goofish.com/",
    # "sec-ch-ua": "\"Chromium\";v=\"146\", \"Not-A.Brand\";v=\"24\", \"Google Chrome\";v=\"146\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    # "sec-gpc": "1",
    "user-agent": generate_user_agent()
}
# with open('cookie', 'r') as file:
#     str_cookie = file.read()
str_cookie = {}
# ast.literal_eval(str_cookie)
# print(json.loads(str_cookie))
# print(eval(str_cookie), type(eval(str_cookie)))
cookies = json.loads(str_cookie)
timestamp = str(int(time.time()) * 1000)
def get_sign(params_json):
    string = cookies['_m_h5_tk'].split('_')[0] + '&' +  timestamp + '&' + '34839810' + '&' + params_json

    # print(string)
    sign = hashlib.md5(string.encode('utf-8')).hexdigest()
    # print(sign)
    return sign


def get_data(sign):
    url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlemtopsearch.pc.search/1.0/"
    params = {
        "jsv": "2.7.2",
        "appKey": "34839810",
        "t": timestamp,
        "sign": sign,
        "v": "1.0",
        "type": "originaljson",
        "accountSite": "xianyu",
        "dataType": "json",
        "timeout": "20000",
        "api": "mtop.taobao.idlemtopsearch.pc.search",
        "sessionOption": "AutoLoginOnly",
        "spm_cnt": "a21ybx.search.0.0",
        "spm_pre": "a21ybx.search.searchInput.0"
    }
    proxies = proxies = {ip_address()[0]: random.choice(ip_address()[1])}
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, proxies=proxies)

    print(response.json())
if __name__ == "__main__":
    keyword = input('输入查询商品名：')
    # data = {
    #     "data": "{\"pageNumber\":1,\"keyword\":\"笔记本电脑\",\"fromFilter\":false,\"rowsPerPage\":30,\"sortValue\":\"\",\"sortField\":\"\",\"customDistance\":\"\",\"gps\":\"\",\"propValueStr\":{},\"customGps\":\"\",\"searchReqFromPage\":\"pcSearch\",\"extraFilterValue\":\"{}\",\"userPositionJson\":\"{}\"}"
    # }
    info = {
        "pageNumber": 1,
        "keyword": keyword,
        "fromFilter": False,
        "rowsPerPage": 30,
        "sortValue": "",
        "sortField": "",
        "customDistance": "",
        "gps": "",
        "propValueStr": {},
        "customGps": "",
        "searchReqFromPage": "pcSearch",
        "extraFilterValue": "{}",
        "userPositionJson": "{}"
    }
    data = {
        "data": str(json.dumps(info, separators=(',', ':')))
    }
    # print(data)
    sign = get_sign(data['data'])
    # data = json.dumps(data, separators=(',', ':'))
    # print(data)
    # print(sign)
    get_data(sign)
