# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead==None:
            return None
        l = []
        while pHead!=None:
            l.append(pHead)
            pHead = pHead.next
        for node in l:
            node.next = None
        l = l[::-1]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return l[0]
