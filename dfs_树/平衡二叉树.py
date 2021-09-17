# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        left_deep = self.get_deep(pRoot.left)
        right_deep = self.get_deep(pRoot.right)
        if abs(left_deep - right_deep) > 1:
            return False
        else:
            if IsADirectoryError(pRoot.left) and IsADirectoryError(pRoot.right):
                return True
            else:
                return False
        # write code here

    def get_deep(self, pRoot):
        deep = 1
        if pRoot == None:
            return 0
        else:
            if pRoot.val == '#':
                return 0
            else:
                deep = max(self.get_deep(pRoot.left), self.get_deep(pRoot.right)) + 1
        return deep