# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-integers-to-choose-from-a-range-i
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-integers-to-choose-from-a-range-i.py
# solution_class: Solution
# submission_id: 022c25b26315448896943f010695042ce0da37c4
# seed: 1802348644

# Time:  O(b)
# Space: O(b)

# math

class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        k = min(int((-1+(1+8*maxSum))**0.5/2), n)  # k = argmax((k+1)*k//2 <= maxSum)
        total = (k+1)*k//2
        result = k
        lookup = set(banned)
        for x in lookup:
            if x <= k:
                total -= x
                result -= 1
        for i in xrange(k+1, n+1):
            if i in lookup:
                continue
            if total+i > maxSum:
                break
            total += i
            result += 1
        return result