import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #深度优先解法
    def deepestLeavesSum(self, root):
        maxLevel, sum = -1,0
        def recursion(node:TreeNode,level:int):
            if node is None:
                return
            # nonlocal,在python3中表示使用方法外的定义的变量,但不是全局变量
            nonlocal maxLevel,sum
            if level > maxLevel:
                maxLevel = level
                sum = node.val
            elif level == maxLevel:
                sum += node.val
            recursion(node.left,level+1)
            recursion(node.right,level+1)
        recursion(root,0)
        return sum

    #广度优先
    def deepestLeavesSum2(self, root):
        q = collections.deque([root])
        while q:
            sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return sum



if __name__ == '__main__':
    s = Solution()
    root=[]
    s.deepestLeavesSum(root)