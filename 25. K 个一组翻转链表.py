# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     25. K 个一组翻转链表
   Description :
   Author :       fengwentao@changjing.ai
   date：          2021/12/26
-------------------------------------------------
   Change Activity:
                   2021/12/26:
-------------------------------------------------
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode,k:int) -> ListNode:
        summyhead = ListNode(0)
        summyhead.next = head
        prev = summyhead

        while head:
            tail = prev

            for i in range(k):
                tail = tail.next
                if not tail:
                    return summyhead.next
            next = tail.next
            head,tail = self.reverse(head,tail)
            #把子链表重新接回原表
            prev.next = head
            tail.next = next
            prev = tail
            head = tail.next

        return summyhead.next


    def reverse(self,head,tail):
        cur,prev = head,tail.next
        while prev != tail:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return tail,head











def show_list(head:ListNode):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

if __name__ == '__main__':
    node5 = ListNode(5)
    node4 = ListNode(4,node5)
    node3 = ListNode(3,node4)
    node2 = ListNode(2,node3)
    node1 = ListNode(1,node2)
    show_list(node1)

    s = Solution()

    result = s.reverseList(node1,2)
    print("-----------------result-----------------")
    show_list(result)