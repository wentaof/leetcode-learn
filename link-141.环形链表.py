# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     link-141
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/7
-------------------------------------------------
   Change Activity:
                   2022/6/7:
-------------------------------------------------
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #暴力循环 hashset
    def hasCycle(self, head: ListNode):
        if not head:
            return False
        s = set()
        while(head):
            if not head in s:
                s.add(head)
                head = head.next
            else:
                return True
        return False

    #快慢指针
    def hasCycle2(self, head: ListNode):
        if not head or not head.next:
            return False
        fast = head.next
        slow = head

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
