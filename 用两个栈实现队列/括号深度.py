# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/22 15:47


class Brackets():
    def __init__(self):
        self.all_list = [0]
        pass

    def get_result(self, string:str):
        i = 0
        while i<(len(string)):
            while i<len(string) and string[i] == '(':
                self.all_list[-1]+=1
                i+=1
            self.all_list.append(self.all_list[-1])
            while i<len(string) and string[i] == ')':
                self.all_list[-1]-=1
                i+=1
        x = []
        for li in self.all_list:
            x.append(li)
        print(max(x))
        pass

string = input()
brackets = Brackets()
brackets.get_result(string)

# input:(())
# output:2