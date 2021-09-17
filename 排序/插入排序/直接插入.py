# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 14:38

# 思想：将排序过程中的元素分为有序区和无序区，从无序区中选择元素插入到有序区对应的位置
def InsertSort(arr, kind):
    if kind=='up':
        for i in range(1, len(arr)):
            temp = arr[i]
            index = i
            for j in range(i):
                if arr[i-j-1]>temp:
                    arr[i-j] = arr[i-j-1]
                    index = i-j-1
            arr[index] = temp
        return arr
    else:
        for i in range(1, len(arr)):
            temp = arr[i]
            index = i
            for j in range(i):
                if arr[i - j - 1] < temp:
                    arr[i - j] = arr[i - j - 1]
                    index = i - j - 1
            arr[index] = temp
        return arr
    pass

# 时间复杂度
# 最坏：O(n^2)
# 最好：O(n^2)
# 平均：O(n^2)

# 空间复杂度：O(1)

# 稳定性：稳定



if __name__ == '__main__':
    kind = 'up'
    arr = [5, 2, 7, 4]
    arr = InsertSort(arr, kind)
    print(arr)