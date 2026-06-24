# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-integers-by-the-number-of-1-bits
# source_path: LeetCode-Solutions-master/Python/sort-integers-by-the-number-of-1-bits.py
# solution_class: Solution
# submission_id: 54b17b0f5581ce361159ed69caebda56d30d6dba
# seed: 246083161

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def popcount(n):  # Time: O(logn) ~= O(1) if n is a 32-bit number
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result
        
        arr.sort(key=lambda x: (popcount(x), x))
        return arr