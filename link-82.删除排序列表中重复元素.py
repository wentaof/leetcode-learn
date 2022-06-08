# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     link-82.删除排序列表中重复元素
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/8
-------------------------------------------------
   Change Activity:
                   2022/6/8:
-------------------------------------------------
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        pre = None
        while head and cur and cur.next  :
            next = cur.next
            if cur.val != next.val:
                pre = cur
                cur = cur.next
            else:
                cur_value = cur.val
                while cur and cur_value == cur.val :
                    cur = cur.next
                if pre:
                    pre.next = cur
                else:
                    head = cur

        return head
    # leecode 答案
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


if __name__ == '__main__':
    # node1 = ListNode(5)
    # node2 = ListNode(4,node1)
    # node3 = ListNode(4,node2)
    # node4 = ListNode(3,node3)
    # node5 = ListNode(3,node4)
    # node6 = ListNode(2,node5)
    # node7 = ListNode(1,node6)
    # node1 = ListNode(3)
    # node2 = ListNode(2,node1)
    # node3 = ListNode(1,node2)
    # node4 = ListNode(1,node3)
    # node7 = ListNode(1,node4)

    node4 = ListNode(2)
    node5 = ListNode(2,node4)
    node7 = ListNode(1,node5)
    s = Solution()
    result = s.deleteDuplicates(node7)
    while(result):
        print(result.val)
        result = result.next