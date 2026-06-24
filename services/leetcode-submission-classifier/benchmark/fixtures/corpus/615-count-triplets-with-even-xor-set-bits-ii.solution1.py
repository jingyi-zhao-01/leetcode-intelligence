# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-triplets-with-even-xor-set-bits-ii
# source_path: LeetCode-Solutions-master/Python/count-triplets-with-even-xor-set-bits-ii.py
# solution_class: Solution
# submission_id: 3ac00a626a1f53cf6570efcd7d58ecbcaa405332
# seed: 770350174

# Time:  O(nlogr), r = max(max(a), max(b), max(c))
# Space: O(1)

# bit manipulation, parity

class Solution(object):
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
        
        cnt = map(count, (a, b, c))
        return sum(cnt[0][0 if i == 0 or i == 1 else 1]*cnt[1][0 if i == 0 or i == 2 else 1]*cnt[2][0 if i == 0 or i == 3 else 1] for i in xrange(4))