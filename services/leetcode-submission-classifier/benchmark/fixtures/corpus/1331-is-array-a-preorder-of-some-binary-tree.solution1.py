# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: is-array-a-preorder-of-some-binary-tree
# source_path: LeetCode-Solutions-master/Python/is-array-a-preorder-of-some-binary-tree.py
# solution_class: Solution
# submission_id: 56d041cbacae409eef5ba1968008996bb119da8f
# seed: 2304657030

# Time:  O(n)
# Space: O(n)

# stack

class Solution(object):
    def isPreorder(self, nodes):
        """
        :type nodes: List[List[int]]
        :rtype: bool
        """
        stk = [nodes[0][0]]
        for i in xrange(1, len(nodes)):
            while stk and stk[-1] != nodes[i][1]:
                stk.pop()                
            if not stk:
                return False            
            stk.append(nodes[i][0])            
        return True