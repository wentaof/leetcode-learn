# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     冒泡排序算法
   Description : 冒泡排序是两个相邻的元素互换
   Author :       fengwentao@changjing.ai
   date：          2022/6/9
-------------------------------------------------
   Change Activity:
                   2022/6/9:
-------------------------------------------------
"""
def bubbleSort(s1):
    if not s1:
        return s1
    size = len(s1)
    for i in range(size):
        for j in range(size - i -1):
            if s1[j] > s1[j+1]:
                temp = s1[j]
                s1[j] = s1[j+1]
                s1[j+1] = temp





l1 = [9,0,6,5,3,10,36,2,1]
print("排序前:%s"% l1)
bubbleSort(l1)
print("排序后:%s"% l1)
