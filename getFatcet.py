#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : getFatcet.py
# @Author  : Richard
# @Time    : 2022/11/5 10:54
# @Software: PyCharm
# @Version : 2.7
# @Email   : shfeiy@qq.com
import requests
from faker_useragent import faker_useragent
import threading
import time
import numpy as np
from requests.adapters import HTTPAdapter

fk = faker_useragent

def getWS():
    ws = []
    with open(r"C:\Users\edz\ws_4.txt",'r') as f:
        wsDetails = f.readlines()
        for i in wsDetails:
            ws.append(i[:-1].split(',')[1])
    return ws

def getFaucet(ws,num):
    url = 'https://testnet-faucet.gitshock.com/api/claim'
    header_fk = {
        'User-Agent': fk.get_agent(),
        'Host': 'testnet-faucet.gitshock.com',
        'Referer': 'https://testnet-faucet.gitshock.com/'
    }
    param = {
        "address": ws
    }
    s = requests.Session()
    a = HTTPAdapter(max_retries=3)
    b = HTTPAdapter(max_retries=3)
    # 将重试规则挂载到http和https请求
    s.mount('http://', a)
    s.mount('https://', b)
    re = s.post(url=url, headers=header_fk, data=param)
    print(num, re.status_code, re.text)
    if re.status_code == 503:
        print("~~~~~~~~~~~~~~~~~~~~~~",param['address'])
        return param['address']
    else:
        return None

def addwrite(aa,args):
    filePath = r'C:\Users\edz\Desktop\excel数据\web3' #生成的钱包文件存放地址
    if len(aa) > 0:
        with open(filePath + '\\undone_' + 'os.path.basename(__file__).split(".")[0]' + '_' + str(args) + '.csv', 'w') as f:
            for i in range(len(aa)):
                line = aa[i] + '\n'
                f.write(line)
    else:
        return

# 需要多线程运行的函数
def fun(args):
    ws = getWS()
    arr = np.array(ws)  # a is input list
    out = np.split(arr, 10)
    num = 1
    undones = []
    for i in  out[args-1]:
        undo = getFaucet(i,num)
        if undo != None:
            undones.append(undo)
        num = num + 1
    addwrite(undones,args)



if __name__ == '__main__':
    start_time = time.time()
    t1 = threading.Thread(target=fun, args=(1,))
    t2 = threading.Thread(target=fun, args=(2,))
    t3 = threading.Thread(target=fun, args=(3,))
    t4 = threading.Thread(target=fun, args=(4,))
    t5 = threading.Thread(target=fun, args=(5,))
    t6 = threading.Thread(target=fun, args=(6,))
    t7 = threading.Thread(target=fun, args=(7,))
    t8 = threading.Thread(target=fun, args=(8,))
    t9 = threading.Thread(target=fun, args=(9,))
    t10 = threading.Thread(target=fun, args=(10,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()