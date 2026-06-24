# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-triplets-with-even-xor-set-bits-i
# source_path: LeetCode-Solutions-master/Python/count-triplets-with-even-xor-set-bits-i.py
# solution_class: Solution3
# submission_id: 077a4d54a741c8257ab3ff6922b81ed0fee9cbd6
# seed: 391959778

# Time:  O(nlogr), r = max(max(a), max(b), max(c))
# Space: O(1)

# bit manipulation, parity

class Solution3(object):
    def tripletCount(self, a, b, c):
        """
        :type a: List[int]
        :type b: List[int]
        :type c: List[int]
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        return sum(popcount(x^y^z)%2 == 0 for x in a for y in b for z in c)