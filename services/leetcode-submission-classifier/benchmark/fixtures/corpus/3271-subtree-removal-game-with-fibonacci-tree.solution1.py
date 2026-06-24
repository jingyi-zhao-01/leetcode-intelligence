# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-removal-game-with-fibonacci-tree
# source_path: LeetCode-Solutions-master/Python/subtree-removal-game-with-fibonacci-tree.py
# solution_class: Solution
# submission_id: bd67672e6272496b0e60c83fd4f5e93339a74ccf
# seed: 330411385

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        # a pattern appears every 6 grundy numbers in binary forms:
        # 0000,       (0000)01,       (0000)11,                 ((0000)^(0000+1))10,       (0000)11,       (0000)11
        # 0000,     (0000+1)01,     (0000+1)11,           ((0000+1)^((0000+1)+1))10,     (0000+1)11,     (0000+1)11
        # 0000, ((0000+1)+1)01, ((0000+1)+1)11,   (((0000+1)+1)^(((0000+1)+1)+1))10, ((0000+1)+1)11, ((0000+1)+1)11
        # ...
        # 0000,       (XXXX)01,       (XXXX)11,                 ((XXXX)^(XXXX+1))10,       (XXXX)11,       (XXXX)11
        # 0000,     (XXXX+1)01,     (XXXX+1)11,           ((XXXX+1)^((XXXX+1)+1))10,     (XXXX+1)11,     (XXXX+1)11
        # => grundy[6k+1] = 0
        #    grundy[6k+2] = 4k+1
        #    grundy[6k+3] = 4k+3
        #    grundy[6k+4] = 4(k^(k+1))+2
        #    grundy[6k+5] = 4k+3
        #    grundy[6k+6] = 4k+3
        return n%6 != 1