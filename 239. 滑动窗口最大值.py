# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     239. 滑动窗口最大值
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/30
-------------------------------------------------
   Change Activity:
                   2021/12/30:
-------------------------------------------------
"""
import heapq
class Solution:

    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans





if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(s.maxSlidingWindow(nums, k))