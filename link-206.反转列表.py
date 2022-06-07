# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     206
   Description :给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
   Author :       fengwentao@changjing.ai
   date：          2021/12/21
-------------------------------------------------
   Change Activity:
                   2021/12/21:
-------------------------------------------------
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head,None
        while cur:
            # cur.next, prev,cur = prev,cur,cur.next
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2,node1)
    node3 = ListNode(3,node2)
    node4 = ListNode(4,node3)
    node5 = ListNode(5,node4)
    print(node5)

    s = Solution()
    result = s.reverseList(node5)
    while(result.val != None):
        print(result.val)
        result = result.next