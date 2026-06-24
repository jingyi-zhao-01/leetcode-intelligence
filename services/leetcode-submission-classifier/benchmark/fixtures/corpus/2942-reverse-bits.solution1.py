# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-bits
# source_path: LeetCode-Solutions-master/Python/reverse-bits.py
# solution_class: Solution
# submission_id: 05acf89d865372450de94ee59e1fbd1b12e88701
# seed: 3742627551

# Time : O(32)
# Space: O(1)

class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n