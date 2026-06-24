# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-integers-to-choose-from-a-range-i
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-integers-to-choose-from-a-range-i.py
# solution_class: Solution3
# submission_id: a1b2e62e20854cee36e35244662be47bf989844b
# seed: 1390628786

# Time:  O(b)
# Space: O(b)

# math

class Solution3(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        lookup = set(banned)
        result = total = 0
        for i in xrange(1, n+1):
            if i in lookup:
                continue
            if total+i > maxSum:
                break
            total += i
            result += 1
        return result