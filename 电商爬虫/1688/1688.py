# !/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author:Euler
@Software:PyCharm
@Time    :2026/4/30 12:47
@Project:Project
@File    : 1688
@Description:

"""
import json
from pprint import pprint
import requests,time, execjs
from urllib.parse import quote


class Spider(object):
    def __init__(self, keyword):
        """
        初始值
        """
        self.keyword = keyword
        self.headers = {
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-type": "application/x-www-form-urlencoded",
            "Origin": "https://s.1688.com",
            "Referer": "https://s.1688.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
            "dnt": "1",
            "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-gpc": "1"
        }
        self.t = str(int(time.time() * 1000))
        self.cookies = {
            "leftMenuLastMode": "COLLAPSE",
            "mtop_partitioned_detect": "1",
            "_m_h5_tk": "e3c048c9cd1e59da1f2a3dfda21cf76e_1777531661680",
            "_m_h5_tk_enc": "b110fe32a8104676cc122d4ea55e7603",
            "leftMenuModeTip": "shown",
            "cna": "7sx5IhjKY2EBASQJilAEmUWl",
            "plugin_home_downLoad_cookie": "%E4%B8%8B%E8%BD%BD%E6%8F%92%E4%BB%B6",
            "cookie2": "260c0dc1767854daf228201c7edc8a91",
            "t": "31b35599ff5279469bb1e8191e9e4fb3",
            "_tb_token_": "e37a87e5e3e91",
            "lid": "tb180186028",
            "cookie1": "VAXb3KIDCX997VEXx31aYr1vzBLQk%2FSrpErylhezHic%3D",
            "cookie17": "UUphzOff%2BfVeDyx3%2FA%3D%3D",
            "sgcookie": "E100R3FnAWiW9n4vj7%2FN2X5BKxIzmGikwhMW9QKnrNrMM9cxSYyzrV3yBULjokXNiTjMlx9R%2FINFsQW0moNzyay4vJBf%2BbKgvgYo4WJVAB%2FhSFM%3D",
            "sg": "815",
            "csg": "66387e1c",
            "unb": "2206510005051",
            "uc4": "nk4=0%40FY4PZP%2FgR1i4E8ykdevZvZeqA3AWLA%3D%3D&id4=0%40U2grF8wSVFladXPuCt%2BU1G4x6R6EHUE9",
            "_nk_": "tb180186028",
            "last_mid": "b2b-2206510005051757d7",
            "_csrf_token": "1777524472925",
            "__cn_logon__": "true",
            "__cn_logon_id__": "tb180186028",
            "__last_loginid__": "b2b-2206510005051757d7",
            "__last_memberid__": "b2b-2206510005051757d7",
            "isg": "BO3tuk3KeL7F0BzSQVJBPnR0_IlnSiEck0ax-S_yKQTzpg1Y95ox7Dtkk3pAQjnU",
            "keywordsHistory": "%E7%BA%AF%E9%BB%91%E8%BF%90%E5%8A%A8%E9%9E%8B",
            "_user_vitals_session_data_": "{\"user_line_track\":true,\"ul_session_id\":\"0cx1i4sww3c\",\"last_page_id\":\"s.1688.com%2Fykbzni6fs58\"}"
        }
        self.params = {
            "jsv": "2.7.4",
            "appKey": "12574478",
            "t": self.t,
            "api": "mtop.relationrecommend.WirelessRecommend.recommend",
            "v": "2.0",
            "type": "originaljson",
            "timeout": "20000",
            "dataType": "jsonp",
            "callback": "mtopjsonpreqTppId_32517_getOfferList2"
        }
        # self.data = {
        #     "data": "{\"appId\":39799,\"params\":\"{\\\"bizName\\\":\\\"input_suggest\\\",\\\"keyword\\\":\\\"纯黑运动鞋\\\",\\\"verticalProductFlag\\\":\\\"pcmarket\\\",\\\"integrateTrace\\\":true,\\\"type\\\":\\\"offer\\\",\\\"appName\\\":\\\"nodeSearchWork\\\"}\"}"
        # }
        # self.data = {
        #     "data": '{"appId":32517,"params":"{\"beginPage\":\"1\",\"pageSize\":60,\"method\":\"getOfferList\",\"pageId\":\"mqGUVmv2TegvE3J4kbpaAxnteOvZBQyzVaz1oHIOA98y4jzn\",\"verticalProductFlag\":\"pcmarket\",\"searchScene\":\"pcOfferSearch\",\"charset\":\"GBK\",\"spm\":\"a260k.home2025.searchbox.0\",\"keywords\":\"%B4%BF%BA%DA%D4%CB%B6%AF%D0%AC\"}"}'
        # }
    def parser_userinput(self):
        params = {
            "beginPage": 1,
            "pageSize": 60,
            "method": "getOfferList",
            "pageId": "vWemke0Yz1TEPATHoUdSh6J7AODKkiLtwTKHNFmaEPYFFRea",
            "verticalProductFlag": "pcmarket",
            "searchScene": "pcOfferSearch",
            # "charset": "GBK",
            "charset": "UTF-8",
            "spm": "a26352.13672862.searchbox.0",
            "keywords": quote(keyword)
            # "keywords": quote(keyword, encoding='gbk')
        }
        data = {
            "appId": 32517,
            "params": json.dumps(params, separators=(',', ':'))
        }
        result = json.dumps(data, separators=(',', ':'))
        return result
    def parser_sign(self):
        """
        sign = function u(e)
        e = (o.token + "&" + c + "&" + s + "&" + n.data)
        o.token:_m_h5_tk
        c:t
        s:appKey
        data:data
        :return: sign
        """
        # o_c = self.cookies['_m_h5_tk'].replace("_", "&")
        o = self.cookies['_m_h5_tk'].split('_')[0]
        c = self.t
        s = self.params['appKey']
        data = self.parser_userinput()
        s = o + "&" + c + "&" + s + "&" + data
        # print(s)
        js_code = execjs.compile(open('aef.js', encoding='utf-8').read())
        sign = js_code.call("u", s)
        # print(sign)
        return sign

    def parser_starturl(self):
        url = "https://h5api.m.1688.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
        params = self.params
        params['sign'] = self.parser_sign()
        params['params'] = json.dumps(params, separators=(',', ':'))
        params['data'] = self.parser_userinput()
        response = requests.post(url=url, headers=self.headers, cookies=self.cookies, params=params).json()
        pprint(response)




if __name__ == "__main__":
    keyword = input('输入查询词:')
    s = Spider(keyword=keyword)
    s.parser_starturl()
