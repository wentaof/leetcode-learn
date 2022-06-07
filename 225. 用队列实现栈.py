# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     225. 用队列实现栈
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/29
-------------------------------------------------
   Change Activity:
                   2021/12/29:
-------------------------------------------------
"""
import queue
class MyStack:

    def __init__(self):
        self.q_main = queue.Queue()
        self.q_plugin = queue.Queue()

    def push(self, x: int) -> None:
        while not self.empty():
            self.q_plugin.put(self.q_main.get())
        self.q_main.put(x)
        while not self.q_plugin.empty():
            self.q_main.put(self.q_plugin.get())

    def pop(self) -> int:
        return self.q_main.get()

    def top(self) -> int:

        if not self.empty():
            while not self.q_main.empty():
                self.q_plugin.put(self.q_main.get())
            top = self.q_plugin.get()
            self.q_main.put(top)
            while not self.q_plugin.empty():
                self.q_main.put( self.q_plugin.get())
            return top
        else:
            return None


    def empty(self) -> bool:
        return self.q_main.empty()

if __name__ == '__main__':
    myStack = MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top();
    myStack.pop();
    myStack.empty();
