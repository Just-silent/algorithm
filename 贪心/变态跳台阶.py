# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2020/11/27 19:21

# 知识点：递归，动态规划，递推

# 设f[i] 表示 当前跳道第 i 个台阶的方法数。那么f[n]就是所求答案。
# 假设现在已经跳到了第 n 个台阶，那么前一步可以从哪些台阶到达呢？
# 如果上一步跳 1 步到达第 n 个台阶，说明上一步在第 n-1 个台阶。已知跳到第n-1个台阶的方法数为f[n-1]
# 如果上一步跳 2 步到达第 n 个台阶，说明上一步在第 n-2 个台阶。已知跳到第n-2个台阶的方法数为f[n-2]
# 。。。
# 如果上一步跳 n 步到达第 n 个台阶，说明上一步在第 0 个台阶。已知跳到 第0个台阶的方法数为f[0]
# 那么总的方法数就是所有可能的和。也就是f[n] = f[n-1] + f[n-2] + ... + f[0]
# 显然初始条件f[0] = f[1] = 1
# 所以我们就可以先求f[2]，然后f[3]...f[n-1]， 最后f[n]

# 那么f[n-1] 为多少呢？
# # f[n-1] = f[n-2] + f[n-3] + ... + f[0]
# # 所以一合并，f[n] = 2*f[n-1]，初始条件f[0] = f[1] = 1
# # 所以可以采用递归，记忆化递归，动态规划，递推。具体详细过程，可查看青蛙跳台阶。

import math

class Solution:
    def jumpFloorII(self, number):
        if number == 0 or number == 1:
            return 1
        else:
            return int(math.pow(2, number - 1))
        # write code here

x = int(input())
solution = Solution()
print(solution.jumpFloorII(x))