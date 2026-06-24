# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisible-and-non-divisible-sums-difference
# source_path: LeetCode-Solutions-master/Python/divisible-and-non-divisible-sums-difference.py
# solution_class: Solution2
# submission_id: d8279ff9010f1ac76e673abacc33d3c9deeae68c
# seed: 3463323529

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return (n+1)*n//2 - 2*(((n//m+1)*(n//m)//2)*m)