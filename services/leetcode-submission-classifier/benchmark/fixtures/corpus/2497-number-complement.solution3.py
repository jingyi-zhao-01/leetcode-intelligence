# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-complement
# source_path: LeetCode-Solutions-master/Python/number-complement.py
# solution_class: Solution3
# submission_id: 007c31659060cd7f528ce487edbe85fd3d25c41a
# seed: 3159104348

# Time:  O(1)
# Space: O(1)

class Solution3(object):
    def findComplement(self, num):
        bits = '{0:b}'.format(num)
        complement_bits = ''.join('1' if bit == '0' else '0' for bit in bits)
        return int(complement_bits, 2)