# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: how-many-apples-can-you-put-into-the-basket
# source_path: LeetCode-Solutions-master/Python/how-many-apples-can-you-put-into-the-basket.py
# solution_class: Solution
# submission_id: b7d87a6c2bf8f577206a6b14fbd7ef3484b6245a
# seed: 2740121793

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        LIMIT = 5000
        arr.sort()
        result, total = 0, 0
        for x in arr:
            if total+x > LIMIT:
                break
            total += x
            result += 1
        return result