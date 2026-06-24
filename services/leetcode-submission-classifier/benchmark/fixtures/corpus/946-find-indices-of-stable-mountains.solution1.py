# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-indices-of-stable-mountains
# source_path: LeetCode-Solutions-master/Python/find-indices-of-stable-mountains.py
# solution_class: Solution
# submission_id: 4eb90eb696a6fe948bb48eface640f9a101bde30
# seed: 808421247

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        return [i for i in xrange(1, len(height)) if height[i-1] > threshold]