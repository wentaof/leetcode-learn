# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1037.有效回旋镖
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/8
-------------------------------------------------
   Change Activity:
                   2022/6/8:
-------------------------------------------------
"""
class Solution:
    def isBoomerang(self, points) -> bool:
        p0 = points[0]
        p1 = points[1]
        p2 = points[2]
        (a,b,c) = self.getLinearEquation(p0[0],p0[1],p1[0],p1[1])
        return p2[0] * a + p2[1] * b + c != 0


    # a*x+b*y+c = 0
    def getLinearEquation(self,p1x, p1y, p2x, p2y):
        sign = 1
        a = p2y - p1y
        if a < 0:
            sign = -1
            a = sign * a
        b = sign * (p1x - p2x)
        c = sign * (p1y * p2x - p1x * p2y)
        return [a, b, c]


if __name__ == '__main__':
    s = Solution()
    points = [[1,1],[2,2],[1,3]]
    print(s.isBoomerang(points))