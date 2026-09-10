# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def avg_func(root):
            if not root:
                return (0,0)
            left_count,left_sum = avg_func(root.left)
            right_count,right_sum = avg_func(root.right)

            count = 1+left_count+right_count
            total = root.val+left_sum+right_sum

            return [count,total]
        count = 0
        def trav(root):
            nonlocal count
            if not root:
                return
            avg = avg_func(root)
            if avg[1]//avg[0]==root.val:
                count+=1
            trav(root.right)
            trav(root.left)
        trav(root)
        return count