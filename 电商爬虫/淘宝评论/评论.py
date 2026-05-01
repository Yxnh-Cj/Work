"""
[课程内容]: python实现淘宝商品评论数据采集

[授课老师]: 青灯教育-自游   [授课时间]: 20:00 可以点歌  可以问问题

[环境使用]:
    Python 3.10
    Pycharm

[模块使用]:
    requests
    hashlib
    csv

win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学, 20:00 正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信 python10010

"""
import random

# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入序列化模块
import json
# 导入csv模块
import csv
# 导入哈希模块
import hashlib
# 导入时间模块
import time
from ip_agent import ip_address
from user_agent import generate_user_agent

with open('cookie', 'r') as file:
    str_cookie = file.read()
cookies = json.loads(str_cookie)
# 获取sign加密参数
def get_sign(c, page):
    # token = '1e4c95605ed73b4c637b117ca9a37565'
    token = cookies['_m_h5_tk'].split('_')[0]
    n_data = '{"showTrueCount":false,"auctionNumId":"944730844026","pageNo":%d,"pageSize":20,"orderType":"","searchImpr":"-8","expression":"","skuVids":"","rateSrc":"pc_rate_list","rateType":""}' % page
    string = token + "&" + str(c) + "&" + '12574478' + "&" + n_data
    sign = hashlib.md5(string.encode('utf-8')).hexdigest()
    return sign



# 创建文件对象
f = open('柠檬片.csv', mode='w', encoding='utf-8', newline='')
# 字典写入的方法
csv_writer = csv.DictWriter(f, fieldnames=[
    '昵称',
    '商品标题',
    '产品',
    '日期',
    '评论',
])
# 写入表头
csv_writer.writeheader()
"""发送请求"""
# 模拟浏览器
headers = {
    # cookie 用户信息, 常用于检测是否有登陆账号(登陆与否都有cookie)
    # "cookie": "cookie",
    # referer 防盗链, 告诉服务器请求网址从哪里跳转过来 (遇到403添加防盗链)
    "referer": "https://detail.tmall.com/",
    # user-agent 用户代理, 表示浏览器/设备基本身份信息
    "user-agent":generate_user_agent()
}
# 请求网址
url = 'https://h5api.m.tmall.com/h5/mtop.taobao.rate.detaillist.get/6.0/'
# 构建循环翻页
for page in range(1, 2):
    print(f'正在采集第{page}页的数据内容')
    # 获取当前时间戳
    t = int(time.time() * 1000)
    # 获取加密sign参数
    sign = get_sign(t, page)
    # 查询参数
    params = {
        "jsv": "2.7.5",
        "appKey": "12574478",
        "t": f"{t}",
        "sign": sign,
        "_bx-login": "new",
        "api": "mtop.taobao.rate.detaillist.get",
        "v": "6.0",
        "isSec": "0",
        "ecode": "1",
        "timeout": "20000",
        "dataType": "jsonp",
        "valueType": "string",
        "type": "jsonp",
        "callback": "mtopjsonp28",
        "data": '{"showTrueCount":false,"auctionNumId":"944730844026","pageNo":%d,"pageSize":20,"orderType":"","searchImpr":"-8","expression":"","skuVids":"","rateSrc":"pc_rate_list","rateType":""}' % page
    }
    # 发送请求
    proxies = {ip_address()[0]: random.choice(ip_address()[1])}
    response = requests.get(url=url, params=params, cookies=cookies, proxies=proxies, headers=headers)

    """获取数据"""
    # 获取响应的文本数据  mtopjsonp28({...}) 选择使用字符串方法
    text = response.text
    # print(text)
    """解析数据"""
    # 提取json数据格式
    text_json = re.findall('mtopjsonp28\((.*)', text)[0][:-1]
    # 转成json字典数据
    json_data = json.loads(text_json)
    # 第一次提取评论信息所在的列表
    rateList = json_data['data']['rateList']
    # for循环遍历, 提取列表里面的元素
    for index in rateList:
        # 提取数据保存字典
        dit = {
            '昵称': index['reduceUserNick'],
            '商品标题': index['auctionTitle'],
            '产品': index['skuValueStr'],
            '日期': index['feedbackDate'],
            '评论': index['feedback'],
        }
        # 写入数据
        csv_writer.writerow(dit)
        print(dit)
