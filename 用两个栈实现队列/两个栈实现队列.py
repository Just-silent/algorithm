# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/9/20 19:37


class Solution():

    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self, node):
        # write code here
        self._stack1.append(node)

    def pop(self):
        # return xx
        if self._stack2 == []:
            for i in range(len(self._stack1)):
                node = self._stack1.pop()
                self._stack2.append(node)
        return self._stack2.pop()


solution = Solution()
