# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     learn_heapq
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/30
-------------------------------------------------
   Change Activity:
                   2021/12/30:
-------------------------------------------------
"""
import heapq as hq
import numpy as np
data = np.arange(10)
np.random.shuffle(data)
print(data)
heap = []
for i in data:
    hq.heappush(heap,i)

print(heap)
hq.heappush(heap,0.5)
print(heap)
print(hq.heappop(heap))
print(hq.heappop(heap))
print(hq.heappop(heap))

heap = [5,8,0,3,6,7,9,1,4,2]
hq.heapify(heap)
print(heap)