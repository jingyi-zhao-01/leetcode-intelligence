# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: put-boxes-into-the-warehouse-i
# source_path: LeetCode-Solutions-master/Python/put-boxes-into-the-warehouse-i.py
# solution_class: Solution
# submission_id: 8f6e9be6e178de85553ed055cf5d695d1d8b97a1
# seed: 3051267954

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
        result = 0
        for h in boxes:
            if h > warehouse[result]:
                continue
            result += 1
            if result == len(warehouse):
                break
        return result