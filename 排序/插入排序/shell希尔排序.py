# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/26 14:39

# 数组分区   插入排序

def ShellSort(arr, kind, ds):
    if kind=='up':
        for d in ds:
            indexs = []
            for i in range(len(arr)):
                if i%d==0:
                    indexs.append(i)
            for i in range(1, len(indexs)):
                temp = arr[indexs[i]]
                index = indexs[i]
                for j in range(i-1, -1, -1):
                    if temp > arr[indexs[j]]:
                        arr[indexs[j+1]] = arr[indexs[j]]
                        index = indexs[j]
                arr[index] = temp
        return arr
    else:
        for d in ds:
            indexs = []
            for i in range(len(arr)):
                if i % d == 0:
                    indexs.append(i)
            for i in range(1, len(indexs)):
                temp = arr[indexs[i]]
                index = indexs[i]
                for j in range(i - 1, -1, -1):
                    if temp < arr[indexs[j]]:
                        arr[indexs[j + 1]] = arr[indexs[j]]
                        index = indexs[j]
                arr[index] = temp
        return arr
    pass

# 时间复杂度
# 最坏：
# 最好：
# 平均：

# 空间复杂度：

# 稳定性：稳定



if __name__ == '__main__':
    kind = 'up'
    d = [5, 3, 1]
    arr = [5, 2, 7, 4]
    arr = ShellSort(arr, kind, d)
    print(arr)