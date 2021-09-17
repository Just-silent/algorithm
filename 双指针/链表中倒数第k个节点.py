# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k==0:
            return None
        indexs = []
        h = head
        while h!=None:
            indexs.append(h)
            h = h.next
        if len(indexs)<k:
            return None
        return indexs[-1*k]
