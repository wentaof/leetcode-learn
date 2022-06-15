# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     选择排序法
   Description :
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
        minvalue_index = i
        for j in range(i,size):
            if(s1[j] < s1[minvalue_index]):
                minvalue_index = j
        temp = s1[i]
        s1[i] = s1[minvalue_index]
        s1[minvalue_index] = temp







l1 = [9,0,6,5,3,10,36,2,1]
print("排序前:%s"% l1)
bubbleSort(l1)
print("排序后:%s"% l1)