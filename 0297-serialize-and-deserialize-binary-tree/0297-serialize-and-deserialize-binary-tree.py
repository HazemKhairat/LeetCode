# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        vals = []
        def helper(root):
            if not root:
                vals.append("*")
                return
            vals.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        
        return " ".join(vals)
        

    def deserialize(self, data):
        data = iter(data.split(' '))

        def helper():
            val = next(data)
            if val == '*':
                return None
            
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))