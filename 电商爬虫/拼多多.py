# !/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author:Euler
@Software:PyCharm
@Time    :2026/3/22 13:08
@Project:Project
@File    : 平多多
@Description:

"""
import requests
# from 代理 import 代理
# print(代理.main())
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept": "application/json, text/javascript",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Origin": "https://pinduoduo.com",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://pinduoduo.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1"
}
url = "https://apiv2.pinduoduo.com/api/gindex/tf/query_tf_goods_info"
params = {
    "tf_id": "TFRQ0v00000Y_13398",
    "page": "1",
    "size": "39",
    "anti_content": "0aqWfxUkMwVes_wzXxuetBedvf_dBq-HjRTMkA_MVigWOS3hCKkRmM1ROdkRDSsRVqWK-Hp621bnH23_2cm7f1DM2Im7kKkBvF98mIB3heMZIkMZMkM9TyfgDRzBGTMvMk7sHf72QUMv8EM34pIMRKktB5g9aJQGqi7N9cwX0pTXr2799IeMvVHvP4PKUPHTxXGQTnn2CCd3lxNC_X0TaXVX-waqqxtpuhoy9CGnMZgslwD32MFvRev3skgMPkbwWp6RjvksVeFRHIsZ-DdffI7w1_bBXD6A24cuKPKvcRoknYBlsCbybmUs3V9OJkVPBT69fbz"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
