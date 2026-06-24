# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-removal-game-with-fibonacci-tree
# source_path: LeetCode-Solutions-master/Python/subtree-removal-game-with-fibonacci-tree.py
# solution_class: Solution2
# submission_id: e05fa99196185fb4a7da3a534d7ab3f4b2288d4e
# seed: 2389018504

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        grundy = [0, 1]  # 0-indexed
        for i in xrange(2, n):
            grundy[i%2] = (grundy[(i-1)%2]+1)^(grundy[(i-2)%2]+1)  # colon principle, replace the branches by a non-branching stalk of length equal to their nim sum
        return grundy[(n-1)%2] > 0