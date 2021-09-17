# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    # s 源字符串
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode != None:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]
