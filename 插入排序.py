# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     插入排序
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/9
-------------------------------------------------
   Change Activity:
                   2022/6/9:
-------------------------------------------------
"""
def InsertSort(arr):
    n = len(arr)
    if n == 1:
        return 1
    for i in range(1,n):
        c1 = arr[i]
        j = i
        while j>0 and c1 <arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = c1



l1 = [9,0,6,5,3,10,36,2,1]
print("排序前:%s"% l1)
InsertSort(l1)
print("排序后:%s"% l1)