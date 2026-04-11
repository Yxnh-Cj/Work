# !/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author:Euler
@Software:PyCharm
@Time    :2026/3/31 23:49
@Project:Project
@File    : ip_agent
@Description:

"""
from random import choice
import requests
from user_agent import generate_user_agent

def ip_address():
    url = 'https://proxy.scdn.io/api/get_proxy.php'
    params = {'protocol':'socks5',
              'count':'20',
              'country_code':'CN'}
    response = requests.get(url=url, params=params)
    proxies_list = response.json()['data']['proxies']
    # print(proxies_list)
    return params['protocol'],proxies_list


def main():
    try:
        print(ip_address())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
