# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 11:08

def quick_sort(arr, kind, left, right):
    if kind=='up':
        if right-left>=1:
            pivot = left
            low = left+1
            high = right
            temp = arr[pivot]
            while low<=high:
                if pivot<low:
                    if arr[high]<temp:
                        arr[pivot] = arr[high]
                        pivot = high
                    high-=1
                else:
                    if arr[low]>temp:
                        arr[pivot] = arr[low]
                        pivot = low
                    low+=1
            arr[pivot] = temp
            quick_sort(arr, kind, left, pivot-1)
            quick_sort(arr, kind, pivot+1, right)
    else:
        if right - left >= 1:
            pivot = left
            low = left + 1
            high = right
            temp = arr[pivot]
            while low <= high:
                if pivot < low:
                    if arr[high] > temp:
                        arr[pivot] = arr[high]
                        pivot = high
                    high -= 1
                else:
                    if arr[low] < temp:
                        arr[pivot] = arr[low]
                        pivot = low
                    low += 1
            arr[pivot] = temp
            quick_sort(arr, kind, left, pivot - 1)
            quick_sort(arr, kind, pivot + 1, right)
    return arr

# 时间复杂度：？
# 最坏：？
# 最好：？
# 平均：？

# 空间复杂度：？

# 稳定性：不稳定

if __name__ == '__main__':
    kind = 'down'
    arr = [5, 2, 7, 4]
    arr = quick_sort(arr, kind, 0, len(arr)-1)
    print(arr)