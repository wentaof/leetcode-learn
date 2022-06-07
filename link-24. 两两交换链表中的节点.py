# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     24. 两两交换链表中的节点
   Description : https://leetcode-cn.com/problems/swap-nodes-in-pairs/
   Author :       fengwentao@changjing.ai
   date：          2021/12/22
-------------------------------------------------
   Change Activity:
                   2021/12/22:
-------------------------------------------------
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #解题思路：因为要知道后面两个节点的信息，所以在开头构造一个节点，用来判断后面两个节点是都存在，已经方便交换数据
        dummyhead = ListNode(0)
        temp = dummyhead
        dummyhead.next = head
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2    # 连上开头
            node1.next = node2.next
            node2.next = node1
            temp = node1   # 指针后移
        return dummyhead.next

