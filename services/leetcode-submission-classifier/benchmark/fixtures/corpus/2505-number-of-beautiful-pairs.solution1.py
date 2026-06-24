# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-beautiful-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-beautiful-pairs.py
# solution_class: Solution
# submission_id: b85a381b2240f320a9ffa04d04797f3a294c7b81
# seed: 1180145178

# Time:  O(nlogr)
# Space: O(1)

# number theory, freq table

class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = 0
        cnt = [0]*10
        for x in nums:
            for i in xrange(1, 10):
                if gcd(i, x%10) == 1:
                    result += cnt[i]
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return result