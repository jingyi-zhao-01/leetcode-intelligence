# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-of-levels-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/average-of-levels-in-binary-tree.py
# solution_class: Solution
# submission_id: 2fd52880e44cd0668fae77d877ad1fd4144f83ab
# seed: 1535403202

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        q = [root]
        while q:
            total, count = 0, 0
            next_q = []
            for n in q:
                total += n.val
                count += 1
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            q = next_q
            result.append(float(total) / count)
        return result