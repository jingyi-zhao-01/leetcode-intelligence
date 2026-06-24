# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-group-all-1s-together
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-group-all-1s-together.py
# solution_class: Solution
# submission_id: d91e0ae2e3d5c4d556a893f2d2145071c8564b5a
# seed: 831085571

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        total_count = sum(data)
        result, count, left = 0, 0, 0
        for i in xrange(len(data)):
            count += data[i]
            if i-left+1 > total_count: 
                count -= data[left]
                left += 1
            result = max(result, count)
        return total_count-result