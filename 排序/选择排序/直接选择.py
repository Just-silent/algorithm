# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 14:38

# 思想：将排序过程中的元素分为有序区和无序区，从无序区中选择最小（最大）元素放入到有序区的末尾

def SelectSort(arr, kind):
    if kind=='up':
        for i in range(len(arr)-1):
            index = i
            for j in range(i+1, len(arr)):
                if arr[j]<arr[index]:
                    index = j
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
        return arr
    else:
        for i in range(len(arr) - 1):
            index = i
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[index]:
                    index = j
            temp = arr[i]
            arr[i] = arr[index]
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
    arr = SelectSort(arr, kind)
    print(arr)