# -*- coding: utf-8 -*-
# @Author   : Just-silent
# @time     : 2021/1/29 10:03

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence)==0:
            return False
        else:
            return self.isbst(sequence)

    def isbst(self, sequence):
        if len(sequence)<=1:
            return True
        else:
            mid = sequence[-1]
            left, right, flag = self.get_both_side(sequence[:-1], mid)
            if flag==False:
                return False
            return (self.isbst(left) and self.isbst(right))

    def get_both_side(self, sequence, mid):
        left = []
        right = []
        for n in sequence:
            if n<mid:
                left.append(n)
            else:
                right.append(n)
        x = left
        x.extend(right)
        if sequence!=x:
            return [], [], False
        else:
            return left, right, True

if __name__ == '__main__':
    solution = Solution()
    sequence = [4,8,6,12,16,14,10]
    print(solution.VerifySquenceOfBST(sequence))