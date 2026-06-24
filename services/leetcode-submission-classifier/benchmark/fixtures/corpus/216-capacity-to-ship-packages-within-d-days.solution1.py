# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: capacity-to-ship-packages-within-d-days
# source_path: LeetCode-Solutions-master/Python/capacity-to-ship-packages-within-d-days.py
# solution_class: Solution
# submission_id: 7eb26d86b85a37082974ed0645dca4da014d7851
# seed: 2602395792

# Time:  O(nlogr)
# Space: O(1)

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def possible(weights, D, mid):
            result, curr = 1, 0
            for w in weights:
                if curr+w > mid:
                    result += 1
                    curr = 0
                curr += w
            return result <= D
    
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right-left)//2
            if possible(weights, D, mid):
                right = mid-1
            else:
                left = mid+1
        return left