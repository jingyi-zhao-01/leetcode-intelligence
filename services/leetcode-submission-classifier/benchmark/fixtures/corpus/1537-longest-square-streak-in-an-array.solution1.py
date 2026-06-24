# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-square-streak-in-an-array
# source_path: LeetCode-Solutions-master/Python/longest-square-streak-in-an-array.py
# solution_class: Solution
# submission_id: 972a6f515036288e73a76bb932cea6e89cd5a959
# seed: 3638309489

# Time:  O(nlogn)
# Space: O(n)

# hash table

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(set(nums))
        squares = {x for x in sorted_nums if x%2 < 2}  # squared_num % 4 in [0, 1] 
        result = 0
        for x in sorted_nums:
            square, cnt = x**2, 1
            while square in squares:
                squares.remove(square)
                cnt += 1
                square *= square
            result = max(result, cnt)
        return result if result != 1 else -1