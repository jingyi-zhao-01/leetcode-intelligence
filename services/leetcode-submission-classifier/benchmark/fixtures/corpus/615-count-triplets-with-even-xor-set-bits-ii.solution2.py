# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-triplets-with-even-xor-set-bits-ii
# source_path: LeetCode-Solutions-master/Python/count-triplets-with-even-xor-set-bits-ii.py
# solution_class: Solution2
# submission_id: d028b684cef3041a4acb5def1792e6db0c50a87d
# seed: 1566277543

# Time:  O(nlogr), r = max(max(a), max(b), max(c))
# Space: O(1)

# bit manipulation, parity

class Solution2(object):
    def tripletCount(self, a, b, c):
        """
        :type a: List[int]
        :type b: List[int]
        :type c: List[int]
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')

        def count(a):
            odd = sum(popcount(x)&1 for x in a)
            return [len(a)-odd, odd]
        
        even1, odd1 = count(a)
        even2, odd2 = count(b)
        even3, odd3 = count(c)
        return even1*even2*even3 + even1*odd2*odd3 + odd1*even2*odd3 + odd1*odd2*even3