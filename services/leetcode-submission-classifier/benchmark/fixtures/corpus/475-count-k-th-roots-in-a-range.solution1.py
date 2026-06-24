# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-k-th-roots-in-a-range
# source_path: LeetCode-Solutions-master/Python/count-k-th-roots-in-a-range.py
# solution_class: Solution
# submission_id: b9fcd11a4a2546e2b27a19241f058478cfc6dbd8
# seed: 1974056373

# Time:  O(logr * logk)
# Space: O(1)

# binary search, fast exponentiation

class Solution(object):
    def countKthRoots(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        def count(right):
            return binary_search_right(0, right, lambda x: x**k <= right)-0+1
        
        return count(r)-count(l-1)