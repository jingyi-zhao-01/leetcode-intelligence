# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-subarray-elements-equal
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-subarray-elements-equal.py
# solution_class: Solution
# submission_id: 163ff6867db8037cf2e66ff15b1aa9ec09561a0b
# seed: 4115273504

# Time:  O(nlogk)
# Space: O(k)

from sortedcontainers import SortedList


# math, two pointers, sliding window, sorted list

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def rebalance(total_left, total_right):
            if len(left)+1 < len(right):
                x, i = right.pop(0)
                total_right -= x
                left.add((-x, -i))
                total_left += x
            elif len(left) > len(right):
                x, i = left.pop(0)
                total_left -= -x
                right.add((-x, -i))
                total_right += -x
            return total_left, total_right

        result = float("inf")
        left = SortedList()
        right = SortedList()
        total_left = total_right = 0
        for i, x in enumerate(nums):
            if left and -left[0][0] > x:
                left.add((-x, -i))
                total_left += x
            else:
                right.add((x, i))
                total_right += x                
            total_left, total_right = rebalance(total_left, total_right)
            if i-(k-1) >= 0:
                result = min(result, (total_right-(right[0][0] if k%2 else 0))-total_left)
                j, y = i-(k-1), nums[i-(k-1)]
                if (-y, -j) in left:
                    left.remove((-y, -j))
                    total_left -= y
                else:
                    right.remove((y, j))
                    total_right -= y
                total_left, total_right = rebalance(total_left, total_right)
        return result