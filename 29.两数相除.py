# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     29.两数相除
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/9
-------------------------------------------------
   Change Activity:
                   2022/6/9:
-------------------------------------------------
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        #判断符号位
        flag = -1
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            flag = 1
        # flag =  -1 if ((dividend^divisor)>>31 & 0x1==1) else 1
        # 这个就是对暴力解法的优化, 每次减数翻倍, 累加次数也翻倍, 这就减少了很多的计算量
        result = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend >= divisor):
            i = 1
            temp = divisor
            while dividend >= temp:
                dividend -= temp
                result += i
                i = i << 1
                temp = temp << 1

        result *= flag
        if result>INT_MAX or result<INT_MIN:
            return INT_MAX
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.divide(7, -3))