'''
Problem: Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Example
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
    1
  0   1
 0 1 0 1 

Note:
1) The number of nodes in the tree is between 1 and 1000.
2) node.val is 0 or 1.
3) The answer will not exceed 2^31 - 1.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

###############################################################
# Solution 1
# 63 / 63 test cases passed. 
# Runtime: 32 ms  (> 93.41%)
# Memory Usage: 14 MB (> 67.05%)
###############################################################

class Solution1:
    
    result:int = 0
    
    def readTree(self, root: TreeNode, path: str) -> int:
        
        path = path + str(root.val)
        
        if root.left:
            self.readTree(root.left, path)
        
        if root.right:
            self.readTree(root.right, path)
        
        if not (root.left or root.right):
            self.result = self.result + int(path, 2)
            #print(path)
            
        return 1
        
    def sumRootToLeaf(self, root: TreeNode) -> int:

        path = ""
        self.readTree(root, path)

        return self.result

###############################################################
# Solution 1a (upgrade from 1)
# 63 / 63 test cases passed. 
# Runtime: 28 ms  (> 98.86%)
# Memory Usage: 13.8 MB (> 99.85%)
###############################################################

class Solution1a:

    def sumRootToLeaf(self, root: TreeNode) -> int:

        path = ""
        self.result = 0
        
        def readTree(root, path):
        
            path = path + str(root.val)

            if root.left:
                readTree(root.left, path)

            if root.right:
                readTree(root.right, path)

            if not (root.left or root.right):
                self.result = self.result + int(path, 2)
        
        readTree(root, path)

        return self.result

###############################################################
# Sample Solution 1  (20 ms)                                  #
###############################################################

class Solution2:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        """
        Same as previous solution, but you the fact that bits
        are base 2 to increment, rather than doing string conversion.
        Recursive DFS to save paths
        """
        self.total = 0
        def DFS(root, binary):
            if root == None:
                return
            binary = binary * 2 + root.val
            if root.left == None and root.right == None:
                self.total += binary
            else:
                DFS(root.left, binary)
                DFS(root.right, binary)
        DFS(root, 0)
        return int(self.total)

###############################################################
# Sample Solution 2  (13728 kb)                               #
###############################################################

class Solution3:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        # recursive (with / without path but summed)
        # def getVal(valList):
        #     summed = 0
        #     for v in valList:
        #         summed <<= 1
        #         summed += v
        #     return summed
        
        final = 0
        # path = []
        summed = 0
        def traverse(node):
            nonlocal final,summed
            if (node is None):
                return
            
            # path.append(node.val)
            summed <<= 1
            summed += node.val
            
            # leaf
            if (not node.left) and (not node.right):
                # v = getVal(path)
                # print(path, v)
                final += summed
            
            traverse(node.left)
            traverse(node.right)
            
            summed -= node.val
            summed >>= 1
            
            # path.pop()
            
        traverse(root)
        return final
    
        
        # iterative (with / without path but summed)
