# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20. 有效的括号
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/29
-------------------------------------------------
   Change Activity:
                   2021/12/29:
-------------------------------------------------
"""
class Solution:
    def isValid(self, s):

        m = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if not c in m.keys():
                stack.append(c)
            elif not stack or m.get(c) != stack.pop():
                return False
        return not stack



if __name__ == '__main__':
    s = Solution()
    str = "()[]{}"
    print(s.isValid(str))