class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cnt = Counter()

        def dfs(root):
            if root == None: return 0
            value = root.val
            cnt[value] = 1 + max(dfs(root.left) , dfs(root.right))
            return cnt[value]
        dfs(root)
        ans = None

        def solve(root):
            nonlocal ans
            if root == None: return

            if root.left == root.right == None:
                ans = root
                return
            elif root.left and not root.right:
                solve(root.left)
            elif root.right and not root.left: 
                solve(root.right)
            else:
                left, right = root.left.val, root.right.val
                if cnt[left] > cnt[right]:
                    solve(root.left)
                elif cnt[right] > cnt[left]:
                    solve(root.right)
                else:
                    ans = root
                    return

        solve(root)
        
        return ans