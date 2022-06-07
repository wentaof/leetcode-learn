# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1.两数之和
   Description :给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
   Author :       fengwentao@changjing.ai
   date：          2022/1/12
-------------------------------------------------
   Change Activity:
                   2022/1/12:
-------------------------------------------------
"""
class Solution:
    # 我自己写的这个比官方给的速度都快 好神奇
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        for idx,num in enumerate(nums):
            other = target - num
            if other in nums[idx+1:]:
                return [idx,nums[idx+1:].index(other) + idx + 1]
        return []

    def twoSum2(self, nums, target):
        d = {}
        for idx,num in enumerate(nums):
            if target - num in d:
                return [d.get(target - num),idx]
            else:
                d[num] = idx
        return []



if __name__ == '__main__':
    s = Solution()
    nums = [3,3]
    target = 6
    print(s.twoSum2(nums,target))
