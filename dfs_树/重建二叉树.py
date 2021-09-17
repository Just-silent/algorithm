# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        head = TreeNode(pre[0])
        head_idx = tin.index(head.val)
        if head_idx is not None:
            head.left = self.reConstructBinaryTree(pre[1:1+head_idx], tin[:head_idx])
        if head_idx is not len(tin)-1:
            head.right = self.reConstructBinaryTree(pre[head_idx+1:], tin[head_idx+1:])
        return head

if __name__ == '__main__':
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]
    solution =Solution()
    head = solution.reConstructBinaryTree(pre, tin)
    print(head)