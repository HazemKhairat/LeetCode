# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = {}
        has_parent = set()

        for p, c, isLeft in descriptions:
            if p not in dic:
                node = TreeNode(p)
                dic[p] = node
            if c not in dic:
                node = TreeNode(c)
                dic[c] = node
            
            if isLeft == 1:
                dic[p].left = dic[c]
            else:
                dic[p].right = dic[c]
            
            has_parent.add(c)

            # print(dic)
            
        for p, c, _ in descriptions:
            if p not in has_parent:
                return dic[p]
            
        return None
            
                
