# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     line-61.旋转列表
   Description :
   Author :       fengwentao@changjing.ai
   date：          2022/6/7
-------------------------------------------------
   Change Activity:
                   2022/6/7:
-------------------------------------------------
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        link = head
        lenth = 0
        while link:
            lenth +=1
            if not link.next:
                link.next = head
                break
            link = link.next

        move_size = (lenth - k) % lenth
        while move_size:
            head = head.next
            move_size -=1
        temp = head
        while lenth:
            if lenth == 1:
                temp.next = None
                break
            temp = temp.next
            lenth -= 1

        return head


    # 上面的优化方案 还没我自己写的快呢
    def rotateRight2(self, head, k):
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        # if (add := n - k % n) == n: python3.8以上支持
        add = n - k % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret




if __name__ == '__main__':
    node1 = ListNode(5)
    node2 = ListNode(4,node1)
    node3 = ListNode(3,node2)
    node4 = ListNode(2,node3)
    node5 = ListNode(1,node4)


    s = Solution()
    result = s.rotateRight(node5,2)
    while(result.val != None):
        print(result.val)
        result = result.next