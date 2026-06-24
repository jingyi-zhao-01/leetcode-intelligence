# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-digits-of-string-after-convert
# source_path: LeetCode-Solutions-master/Python/sum-of-digits-of-string-after-convert.py
# solution_class: Solution
# submission_id: 895a96ed690bb73272f05340df9d3ddb16d2def5
# seed: 12975655

# Time:  O(n + logn + log(logn) + ...) = O(n)
# Space: O(1)

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        total = reduce(lambda total, x: total+sum(divmod((ord(x)-ord('a')+1), 10)), s, 0)
        while k > 1 and total > 9:
            new_total = 0
            while total:
                total, x = divmod(total, 10)
                new_total += x
            total = new_total
            k -= 1
        return total