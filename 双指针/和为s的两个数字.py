# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        s = 0
        e = len(array)-1
        sums = []
        sume = []
        while s<e:
            if array[s]+array[e] == tsum:
                sums.append(array[s])
                sume.append(array[e])
                e -= 1
                s += 1
            else:
                if array[s]+array[e] > tsum:
                    e-=1
                else:
                    s+=1
        if len(sums)==0:
            return []
        elif len(sums)==1:
            return [sums[0], sume[0]]
        else:
            sum_mul = []
            for i in range(len(sums)):
                sum_mul.append(sums[i]*sume[i])
            max_num = min(sum_mul)
            index = sum_mul.index(max_num)
            return [sums[index], sume[index]]

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    tsum = 21
    solution = Solution()
    print(solution.FindNumbersWithSum(array, tsum))