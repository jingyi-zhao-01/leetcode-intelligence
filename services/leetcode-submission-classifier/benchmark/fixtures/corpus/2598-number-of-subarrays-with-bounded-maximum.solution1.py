# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-bounded-maximum
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-bounded-maximum.py
# solution_class: Solution
# submission_id: d81d80b44d2d5d7b87868b11dae03fa720923490
# seed: 58958057

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def count(A, bound):
            result, curr = 0, 0
            for i in A :
                curr = curr + 1 if i <= bound else 0
                result += curr
            return result

        return count(A, R) - count(A, L-1)