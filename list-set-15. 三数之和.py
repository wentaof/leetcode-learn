# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     15. 三数之和
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/1/12
-------------------------------------------------
   Change Activity:
                   2022/1/12:
-------------------------------------------------
"""
class solution:
    # 暴力计算 超出了时间限制
    def threeSum(self,nums) :
        result = []
        size = len(nums)
        # size = 6
        for i in range(0,size):
            for j in range(i + 1,size):
                if -(nums[i] + nums[j]) in nums[j + 1:]:
                    a = [nums[i],nums[j],-(nums[i] + nums[j])]
                    a.sort()
                    if a not in result:
                        result.append(a)
        return result

    def threeSum2(self,nums) :
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i,v in enumerate(nums[:-2]):
            if i >= 1 and nums[i - 1] == v: #跳过两个紧挨着的元素中的后一个,因为第一次就算的时候就算过了
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-x -v ] = 1
                else:
                    res.add((v,-x-v,x))
        return list(res)



    def threeSum3(self,nums) :
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l ,r = i+1, len(nums) - 1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0: l+=1
                elif s > 0: r -= 1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

if __name__ == '__main__':
    s = solution()
    a = [-1,0,1,2,-1,-4]
    print(s.threeSum3(a))