# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-bits
# source_path: LeetCode-Solutions-master/Python/reverse-bits.py
# solution_class: Solution2
# submission_id: 33da6451a1c39ea45a06a61928c27887dcc9e2df
# seed: 4133630307

# Time : O(32)
# Space: O(1)

class Solution2(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result