# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-binary-strings-with-cost-limit
# source_path: LeetCode-Solutions-master/Python/valid-binary-strings-with-cost-limit.py
# solution_class: Solution2
# submission_id: 4a75a2bac8d23c47ebb64e427f31c3dd4f0450db
# seed: 181845877

# Time:  O(n * 2^n)
# Space: O(n)

# backtracking

class Solution2(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        return ["".join('1' if mask&(1<<i) else '0' for i in xrange(n)) for mask in xrange(1<<n) if mask&(mask>>1) == 0 and sum(i for i in xrange(n) if mask&(1<<i)) <= k]