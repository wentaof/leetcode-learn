# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stack-queue-234.回文链表
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/8
-------------------------------------------------
   Change Activity:
                   2022/6/8:
-------------------------------------------------
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        s = []
        cur = head
        while cur:
            s.append(cur.val)
            cur = cur.next
        while head:
            if s.pop() != head.val:
                return False
            head = head.next
        return True