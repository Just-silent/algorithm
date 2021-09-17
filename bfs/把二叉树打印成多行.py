# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == [] or pRoot == None:
            return []
        array = [pRoot]
        reslt = []
        while array != []:
            x = []
            new_array = []
            for node in array:
                x.append(node.val)
                if node.left != None and node.left.val != '#':
                    new_array.append(node.left)
                if node.right != None and node.right.val != '#':
                    new_array.append(node.right)
            array = new_array
            reslt.append(x)
        return reslt