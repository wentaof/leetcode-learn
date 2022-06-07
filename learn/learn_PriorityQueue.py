# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     learn_heap
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/30
-------------------------------------------------
   Change Activity:
                   2021/12/30:
-------------------------------------------------
"""
from queue import Queue
from queue import PriorityQueue
q = Queue()
print(q.empty())
print(q.full())
print(q.put(1))
# print(q.get(1))
print(q.qsize())
###############优先队列（PriorityQueue）的使用###############
"""
队列的变体，按优先级顺序（最低优先）检索打开的条目。
条目通常是以下格式的元组：
插入格式：q.put((priority number, data))
特点：priority number 越小，优先级越高

其他的操作和队列相同
"""
pq = PriorityQueue()
pq.put((2,"冯文涛2"))
pq.put((1,"冯文涛1"))
pq.put((0,"冯文涛0"))
# 输出的时候,会按着优先级返回,不会按着插入的先后顺序去处理
for i in range(pq.qsize()):
    print(pq.get())

