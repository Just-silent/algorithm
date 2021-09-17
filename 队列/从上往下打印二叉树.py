class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root==None:
            return []
        result = []
        l = [root]
        while l!=[]:
            r = []
            next_l = []
            for i in range(len(l)):
                r.append(l[i].val)
                if l[i].left!=None:
                    next_l.append(l[i].left)
                if l[i].right!=None:
                    next_l.append(l[i].right)
            result.extend(r)
            l = next_l
        return result