# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self, nodes):
    #     self.nodes = nodes
    #     self.root = TreeNode(nodes[0])
    #     for node in nodes[1:]:
    #         self.build_Tree(self.root, node)
    #         a=0
    #
    # def build_Tree(self, root, node):
    #     if root == None:
    #         root = TreeNode(node)
    #     if node <= root.val:
    #         self.build_Tree(root.left, node)
    #     else:
    #         self.build_Tree(root.right, node)

    def build_Tree(self, node):
        root = None
        if len(node)==0:
            return None
        elif len(node)==1:
            return TreeNode(node[0])
        else:
            root = TreeNode(node[0])
            if node[1] <= root.val:
                root.left = self.build_Tree(node[1:])
            else:
                root.right = self.build_Tree(node[1:])
        return root

    def Convert(self , pRootOfTree):
        pass

if __name__ == '__main__':
    nodes = [10, 6, 14, 4, 8, 12, 16]
    solution = Solution()
    tree = solution.build_Tree(nodes)
    a=0