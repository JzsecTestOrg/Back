#-*- coding: utf-8 -*-
__author__ = 'jinghua'

import threading, time, httplib2
from LogicTest import LogicTest

# 需要测试的 url 列表，每一次的访问，我们随机取一个
starttime = time.time()
test1=LogicTest()
#test1.main()
for i in  xrange(200):
    t = threading.Thread(target=test1.main)
    t.start()
endtime = time.time()
print endtime - starttime
