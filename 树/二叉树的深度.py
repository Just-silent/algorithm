# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot==None:
            return 0
        deep = 1
        nodes = [pRoot]
        while nodes!=[]:
            n = []
            for node in nodes:
                if node.left!=None and node.left.val!='#':
                    n.append(node.left)
                if node.right!=None and node.right.val!='#':
                    n.append(node.right)
            nodes = n
            deep+=1
        return deep-1
