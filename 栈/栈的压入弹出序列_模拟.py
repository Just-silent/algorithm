# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def IsPopOrder(self, pushV, popV):
        x = []
        while popV != []:
            if x==[]:
                x.append(pushV.pop(0))
            else:
                while x!=[] and x[-1]==popV[0]:
                    del x[-1]
                    del popV[0]
                if pushV==[] and x!=[]:
                    return False
                elif pushV==[] and x==[]:
                    return True
                if x == []:
                    x.append(pushV.pop(0))
                else:
                    while x!=[] and x[-1] != popV[0]:
                        x.append(pushV.pop(0))
            if popV==[]:
                return True

if __name__ == '__main__':
    solution = Solution()
    pushV = [1,2,3,4,5]
    popV = [4,5,3,2,1]
    print(solution.IsPopOrder(pushV, popV))