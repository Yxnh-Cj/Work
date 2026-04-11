import random
from urllib.parse import quote

# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入序列化模块
import json
# 导入格式输出模块
from pprint import pprint
# 导入序列化模块
import json
# 导入哈希模块
import hashlib
# 导入时间模块
import time
# 导入csv模块
import csv
# from ip_agent import ip_address
from user_agent import generate_user_agent

# with open('cookie', 'r') as file:
    # str_cookie = file.read()
# cookies = json.loads(str_cookie)
cookies = {'_m_h5_tk':''}


def test_get_sign(eT, page, bc_offset, nt_offset, totalResults):
    # cookie中的_m_h5_tk参数值
    # token = "ee25fb9576bdfd10bc928dace1862d71"
    # token = re.findall('_m_h5_tk=(.*?)_', cookie)[0]
    token = cookies['_m_h5_tk'].split('_')[0]
    # print(token)
    # headers中的Appkey
    eC = "12574478"
    ep_params = {
        "device": "HMA-AL00",
        "isBeta": "false",
        "grayHair": "false",
        "from": "nt_history",
        "brand": "HUAWEI",
        "info": "wifi",
        "index": "4",
        "rainbow": "",
        "schemaType": "auction",
        "elderHome": "false",
        "isEnterSrpSearch": "true",
        "newSearch": "false",
        "network": "wifi",
        "subtype": "",
        "hasPreposeFilter": "false",
        "prepositionVersion": "v2",
        "client_os": "Android",
        "gpsEnabled": "false",
        "searchDoorFrom": "srp",
        "debug_rerankNewOpenCard": "false",
        "homePageVersion": "v7",
        "searchElderHomeOpen": "false",
        "search_action": "initiative",
        "sugg": "_4_1",
        "sversion": "13.6",
        "style": "list",
        "ttid": "600000@taobao_pc_10.7.0",
        "needTabs": "true",
        "areaCode": "CN",
        "vm": "nw",
        "countryNum": "156",
        "m": "pc",
        "page": page,
        "n": 48,
        "q": quote(product),
        "qSource": "url",
        "pageSource": "a21bo.jianhua/a.search_history.d1",
        "channelSrp": "",
        "tab": "all",
        "pageSize": "48",
        "totalPage": "100",
        "totalResults": totalResults,
        "sourceS": "96",
        "sort": "_coefp",
        "bcoffset": bc_offset,
        "ntoffset": nt_offset,
        "filterTag": "",
        "service": "",
        "prop": "",
        "loc": "",
        "start_price": "null",
        "end_price": "null",
        "startPrice": "null",
        "endPrice": "null",
        "categoryp": "",
        "ha3Kvpairs": "null",
        "myCNA": "XUkUHszwNGYCAa8N4mheVOoT",
        "screenResolution": "2560x1440",
        "userAgent": generate_user_agent(),
        "couponUnikey": "",
        "subTabId": "",
        "np": "",
        "clientType": "h5",
        "isNewDomainAb": "false",
        "forceOldDomain": "false"
    }
    data = {
        "appId": "34385",
        "params": json.dumps(ep_params, separators=(',', ':'))
    }
    ep_data = json.dumps(data, separators=(',', ':'))
    string = token + "&" + str(eT) + "&" + eC + "&" + ep_data
    sign = hashlib.md5(string.encode('utf-8')).hexdigest()
    return sign, ep_data


def test_get_content(page, bc_offset, nt_offset, totalResults):
    """发送请求"""
    # 模拟浏览器
    headers = {
        "referer": "https://s.taobao.com/",
        # "cookie":cookie,
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        "user-agent": generate_user_agent()
    }
    # 请求网址
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
    # proxies = {ip_address()[0]: random.choice(ip_address()[1])}
    proxies = {}
    # 获取当前时间戳
    eT = int(time.time() * 1000)
    sign, ep_data = get_sign(eT, page, bc_offset, nt_offset, totalResults)
    # print(sign, ep_data)
    # 查询参数
    params = {
        "jsv": "2.7.4",
        "appKey": "12574478",
        "t": eT,
        "sign": sign,
        "api": "mtop.relationrecommend.wirelessrecommend.recommend",
        "v": "2.0",
        "timeout": "10000",
        "type": "jsonp",
        "dataType": "jsonp",
        "callback": "mtopjsonp6",
        "data": ep_data,
        "bx-ua": "fast-load"
    }
    # 发送请求
    response = requests.get(url=url, params=params, headers=headers, cookies=cookies, proxies=proxies)
    """获取数据"""
    # 获取响应的文本数据
    text = response.text
    # print(text)
    """解析数据"""
    # 提取json数据
    text_json = re.findall(r'mtopjsonp6\((.*)', text)[0][:-1]
    # print(text_json)

    # 转成字典数据
    json_data = json.loads(text_json)

    # 判断cookies是否过期
    if '令牌过期' in json_data['ret'][0]:
        print('cookie过期了,请重新获取cookie')
        exit()
    # 字典取值, 提取商品信息所在的列表
    try:
        itemsArray = json_data['data']['itemsArray']
    except Exception as e:
        print(e)
        return '','','4800'
    # for循环遍历, 提取列表里面的元素
    for index in itemsArray:
        try:
            area_info = index['procity'].split(' ')
            if len(area_info) == 2:
                area = area_info[0]  # 省份
                city = area_info[1]  # 城市
            else:
                area = area_info[0]  # 省份
                city = '未知'
            # 在循环中提取具体数据信息, 保存字典中
            dit = {
                '标题': index['title'].replace('<span class=H>', '').replace('</span>', ''),
                '商品ID': index['item_id'],
                '店铺': index['nick'],
                '价格': index['price'],
                '省份': area,
                '城市': city,
                '销量': index['realSales'],
            }
            # 写入数据
            csv_writer.writerow(dit)
            # print(dit)
        except:
            pass
    # 获取下一页参数内容
    bc_offset = json_data['data']['mainInfo']['bcoffset']
    nt_offset = json_data['data']['mainInfo']['ntoffset']
    totalResults = json_data['data']['mainInfo']['totalResults']
    return bc_offset, nt_offset, totalResults


# 创建文件对象
product = '手机'
f = open(f'{product}数据.csv', mode='w', encoding='utf-8', newline='')
# 字典写入的方法
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '商品ID',
    '店铺',
    '价格',
    '省份',
    '城市',
    '销量',
])
# 写入表头
csv_writer.writeheader()
bc_offset = ''
nt_offset = ''
totalResults = '4800'
# get_content(1, bc_offset, nt_offset, totalResults)
# 构建循环翻页
for page in range(1, 2):
    print(f'正在采集第{page}页的数据内容')
    bc_offset, nt_offset, totalResults = get_content(page, bc_offset, nt_offset, totalResults)
