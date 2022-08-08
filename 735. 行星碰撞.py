class Solution:
    def asteroidCollision(self, l):
        size = len(l)
        if size < 2:
            return l
        while True:
            size = len(l)
            for i in range(size-1):
                if self.deal(l,i,i+1):
                    break
            size2 = len(l)
            if size == size2:
                break
        return l

    def deal(self,l,start,end):
        start=l[start]
        end = l[end]
        sign = self.sign(start) * self.sign(end)
        if sign < 0:
            #不同方向的要进行处理
            if abs(start) > abs(end):
                l.remove(end)
            elif abs(start) < abs(end):
                l.remove(start)
            else:
                l.remove(end)
                l.remove(start)
            return True
        return False


    def sign(self,num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0

s = Solution()
# r =s.asteroidCollision([10,2,-5])
# r =s.asteroidCollision([8,-8])
# r =s.asteroidCollision([5,10,-5])
r =s.asteroidCollision([-2,-1,1,2])
print(r)