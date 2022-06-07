# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     242.有效的字母异位词
   Description :给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

   Author :       fengwentao@changjing.ai
   date：          2022/1/12
-------------------------------------------------
   Change Activity:
                   2022/1/12:
-------------------------------------------------
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        ds = {}
        for i in s:
            ds[i] = ds.get(i,0) + 1
        dt = {}
        for i in t:
            dt[i] = dt.get(i,0) + 1
        return ds == dt



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    ss = Solution()
    print(ss.isAnagram2(s,t))