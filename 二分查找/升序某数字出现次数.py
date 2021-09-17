# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/27 17:29

class Solution:
    def GetNumberOfK(self, data, k):
        if k not in data:
            return 0
        low = 0
        high = len(data)-1
        mid = (low+high)//2
        while low<high:
            if data[mid]<k:
                low = mid+1
            else:
                high = mid
            mid = (low+high)//2
        s = low
        low = 0
        high = len(data)-1
        while low<high:
            if data[mid]<=k:
                low = mid+1
            else:
                high = mid
            mid = (low+high)//2
        e = low
        if data[e]!=k:
            return e-s
        else:
            return e-s+1
        # write code here

input = input()
k = int(input[-1])
data = input[1:-3].split(',')
for i,num in enumerate(data):
    data[i] = int(num)
solution = Solution()
print(solution.GetNumberOfK(data, k))