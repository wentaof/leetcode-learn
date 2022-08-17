# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [ListNode]):
        # 暴力解法
        head = point = ListNode(0)
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        for v in sorted(vals):
            point.next = ListNode(v)
            point = point.next

        return head.next


    def mergeKLists2(self, lists: [ListNode]):
        # 优先队列
        head = point = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))

        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
