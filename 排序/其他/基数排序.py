# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 14:39

# 思想：依次对个位、十位、百位···排序

def radix_sort(s):
    """基数排序"""
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
        i += 1
    print(s)

if __name__ == '__main__':
    a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    radix_sort(a)