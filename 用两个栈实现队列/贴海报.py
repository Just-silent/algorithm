# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/22 16:23

class Poster():

    def __init__(self):
        self.result_list = []
        pass

    def insert(self, x1, x2):
        if self.result_list == []:
            self.result_list.append([x1, x2])
        else:
            flag = True
            for y1, y2 in self.result_list:
                if y1 >= x1 and x2 >= y2:
                    self.result_list.remove([y1, y2])
            self.result_list.append([x1, x2])
        pass

    def get_result(self):
        return len(self.result_list)


nums = input()
poster = Poster()
for i in range(int(nums)):
    post = input()
    x1, x2 = post.split()
    poster.insert(int(x1), int(x2))
print(poster.get_result())