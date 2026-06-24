# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: put-boxes-into-the-warehouse-ii
# source_path: LeetCode-Solutions-master/Python/put-boxes-into-the-warehouse-ii.py
# solution_class: Solution
# submission_id: f0f4e7b46a27b4ee66b3cf62275667a8666eefc1
# seed: 2864033394

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort(reverse=True)
        left, right = 0, len(warehouse)-1
        for h in boxes:
            if h <= warehouse[left]:
                left += 1
            elif h <= warehouse[right]:
                right -= 1
            if left > right:
                break
        return left + (len(warehouse)-1-right)