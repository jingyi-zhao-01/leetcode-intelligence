# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-removable-characters
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-removable-characters.py
# solution_class: Solution2
# submission_id: e975efbe1ff9aaeec542ff382622d82f9dd843fa
# seed: 1574685350

# Time:  O(rlogn)
# Space: O(r)

# if r = O(1), this is better

class Solution2(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def check(s, p, lookup, x):
            j = 0
            for i in xrange(len(s)):
                if lookup[i] <= x or s[i] != p[j]:
                    continue
                j += 1
                if j == len(p):
                    return True
            return False

        lookup = [float("inf")]*len(s)
        for i, r in enumerate(removable):
            lookup[r] = i+1
        left, right = 0, len(removable)
        while left <= right:
            mid = left + (right-left)//2
            if not check(s, p, lookup, mid):
                right = mid-1
            else:
                left = mid+1
        return right