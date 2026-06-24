# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-substring-with-identical-characters-i
# source_path: LeetCode-Solutions-master/Python/smallest-substring-with-identical-characters-i.py
# solution_class: Solution
# submission_id: 5fd1eb5bc71eb2fcf3cb0c755a6dcf055030e6e2
# seed: 1906428608

# Time:  O(nlogn)
# Space: O(1)

# binary search, greedy

class Solution(object):
    def minLength(self, s, numOps):
        """
        :type s: str
        :type numOps: int
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def lengths():
            cnt = 0
            for i in xrange(len(s)):
                cnt += 1
                if i+1 == len(s) or s[i+1] != s[i]:
                    yield cnt
                    cnt = 0
    
        def check(x):
            if x == 1:
                cnt = sum(int(x) != i%2 for i, x in enumerate(s))
                return min(cnt, len(s)-cnt) <= numOps
            return sum(l//(x+1) for l in lengths()) <= numOps
    
        return binary_search(1, len(s), check)