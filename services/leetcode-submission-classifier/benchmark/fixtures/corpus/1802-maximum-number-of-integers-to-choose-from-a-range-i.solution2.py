# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-integers-to-choose-from-a-range-i
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-integers-to-choose-from-a-range-i.py
# solution_class: Solution2
# submission_id: 22dbed6f541bef18362e1b1fe4b340c2242e5af6
# seed: 296273978

# Time:  O(b)
# Space: O(b)

# math

class Solution2(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        def check(x):
            return (x+1)*x//2-prefix[bisect.bisect_right(sorted_banned, x)] <= maxSum
    
        sorted_banned = sorted(set(banned))
        prefix = [0]*(len(sorted_banned)+1)
        for i in xrange(len(sorted_banned)):
            prefix[i+1] = prefix[i]+sorted_banned[i]
        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right-bisect.bisect_right(sorted_banned, right)