# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-days-to-make-m-bouquets
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-days-to-make-m-bouquets.py
# solution_class: Solution
# submission_id: 7946c28e7fd2410dc210a9c16b31899fd59d429b
# seed: 2523866644

# Time:  O(nlogd), d is the max day of bloomDay
# Space: O(1)

class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def check(bloomDay, m, k, x):
            result = count = 0
            for d in bloomDay:
                count = count+1 if d <= x else 0
                if count == k:
                    count = 0
                    result += 1
                    if result == m:
                        break
            return result >= m

        if m*k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = left + (right-left)//2
            if check(bloomDay, m, k, mid):
                right = mid-1
            else:
                left = mid+1
        return left