# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-complement
# source_path: LeetCode-Solutions-master/Python/number-complement.py
# solution_class: Solution2
# submission_id: e9574bfcc7c5a7a2d0c04a2a08ed3694f197b882
# seed: 531954054

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num