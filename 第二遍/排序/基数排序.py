# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

# 思想：依次对个位、十位、百位···排序

def radix_sort(s):
    """基数排序"""
    max_len = len(str(max(s)))
    d = 1
    while max_len:
        arr = [[] for i in range(10)]
        for n in s:
            arr[int(n//d%10)].append(n)
        d*=10
        max_len-=1
        temp = []
        for a in arr:
            temp.extend(a)
        s = temp
    print(s)

if __name__ == '__main__':
    a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    radix_sort(a)