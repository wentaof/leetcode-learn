# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     快速排序
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/9
-------------------------------------------------
   Change Activity:
                   2022/6/9:
-------------------------------------------------
"""
def Movepoivt(arr,low,high):
    Pivot = arr[high]
    imove = (low - 1)
    for i in range(low, high):
        if arr[i] <= Pivot:
            imove += 1