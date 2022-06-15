# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     703. 数据流中的第 K 大元素
   Description :设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

   Author :       fengwentao@changjing.ai
   date：          2021/12/30
-------------------------------------------------
   Change Activity:
                   2021/12/30:
实现机制:
    1.heap堆: Binary,Binomial,Fibonacci
    2.二分查找
-------------------------------------------------
"""
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.l = []
        self.l += nums
        self.k = k
    def add(self, val: int) -> int:
        self.l.append(val)
        self.l.sort(reverse=True)
        self.l = self.l[:self.k]
        return self.l[-1]

class KthLargest2:
    """优先队列做法"""
    def __init__(self, k: int, nums):
        self.l = []
        self.k = k
        self.l += nums
        heapq.heapify(self.l)

    def add(self, val: int) -> int:
        heapq.heappush(self.l,val)
        while len(self.l) > self.k:
            heapq.heappop(self.l)
        return self.l[0]

kthLargest = KthLargest2(3, [4, 5, 8, 2]);
print(kthLargest.add(3)) # return 4
print(kthLargest.add(5)) #5
print(kthLargest.add(10))#5
print(kthLargest.add(9))#8
print(kthLargest.add(4))#8
