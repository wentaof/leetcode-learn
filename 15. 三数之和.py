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
            if i >= 1 and nums[i - 1] == v:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-x -v ] = 1
                else:
                    res.add((v,-x-v,x))
        return list(res)


if __name__ == '__main__':
    s = solution()
    a = [-1,0,1,2,-1,-4]
    print(s.threeSum2(a))