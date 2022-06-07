# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     232. 用栈实现队列
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/29
-------------------------------------------------
   Change Activity:
                   2021/12/29:
-------------------------------------------------
"""
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []


    def push(self, x: int):
        self.push_stack.append(x)

    def pop(self) :
        peek_int = self.peek()
        self.pop_stack.remove(peek_int)
        return peek_int

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        elif (not self.pop_stack) and self.push_stack:
            for i in self.push_stack[::-1]:
                self.pop_stack.append(i)
            self.push_stack = []
            return self.pop_stack[-1]
        return None


    def empty(self):
        return len(self.push_stack) + len( self.pop_stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == '__main__':
    myQueue = MyQueue();
    myQueue.push(1); # queue is: [1]
    #myQueue.push(2); # queue is: [1, 2] (leftmost is front of the queue)
    #myQueue.peek(); # return 1
    myQueue.pop(); # return 1, queue is [2]
    myQueue.empty(); # return false


