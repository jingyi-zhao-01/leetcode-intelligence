# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-removable-characters
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-removable-characters.py
# solution_class: Solution
# submission_id: 33a01950b668b5d609c138cd3d6f95812e3992b4
# seed: 2124740006

# Time:  O(rlogn)
# Space: O(r)

# if r = O(1), this is better

class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def check(s, p, removable, x):
            lookup = set(removable[i] for i in xrange(x))
            j = 0
            for i in xrange(len(s)):
                if i in lookup or s[i] != p[j]:
                    continue
                j += 1
                if j == len(p):
                    return True
            return False

        left, right = 0, len(removable)
        while left <= right:
            mid = left + (right-left)//2
            if not check(s, p, removable, mid):
                right = mid-1
            else:
                left = mid+1
        return right