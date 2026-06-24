# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: put-boxes-into-the-warehouse-i
# source_path: LeetCode-Solutions-master/Python/put-boxes-into-the-warehouse-i.py
# solution_class: Solution2
# submission_id: e4724758b30f7988d378dfec79dd20449ed9acd0
# seed: 298725140

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort()
        for i in xrange(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        result, curr = 0, 0
        for h in reversed(warehouse):
            if boxes[curr] > h:
                continue
            result += 1
            curr += 1
            if curr == len(boxes):
                break
        return result