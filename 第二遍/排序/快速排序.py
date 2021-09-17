# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 11:08

# 快速排序： 选定分界值，然后将数组分为两部分，递归，直至无法切分

def quick_sort(arr, kind, left, right):
    if kind=='up':
        if right - left >= 1:
            index = left
            temp = arr[left]
            l = left+1
            r = right
            while l<=r:
                if arr[r]>=arr[index]:
                    r-=1
                else:
                    arr[index] = arr[r]
                    index = r
                if arr[l]<=arr[index]:
                    l+=1
                else:
                    arr[index] = arr[l]
                    index = l
            arr[index] = temp
            quick_sort(arr, 'up', left, index-1)
            quick_sort(arr, 'up', index+1, right)
    else:
        pass
    return arr

# 时间复杂度：？
# 最坏：？
# 最好：？
# 平均：？

# 空间复杂度：？

# 稳定性：不稳定

if __name__ == '__main__':
    kind = 'up'
    arr = [5, 2, 7, 4]
    arr = quick_sort(arr, kind, 0, len(arr)-1)
    print(arr)