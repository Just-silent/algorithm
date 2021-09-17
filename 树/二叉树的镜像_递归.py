# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root==None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)