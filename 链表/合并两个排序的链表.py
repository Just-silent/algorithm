# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1==None and pHead2==None:
            return None
        l = []
        while (pHead1!=None or pHead2!=None):
            if pHead1==None:
                while pHead2!=None:
                    l.append(pHead2)
                    pHead2 = pHead2.next
            elif pHead2==None:
                while pHead1!=None:
                    l.append(pHead1)
                    pHead1 = pHead1.next
            else:
                if pHead1.val<=pHead2.val:
                    l.append(pHead1)
                    pHead1 = pHead1.next
                else:
                    l.append(pHead2)
                    pHead2 = pHead2.next
        for node in l:
            node.next = None
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return l[0]