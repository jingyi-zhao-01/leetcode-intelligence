# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-move-all-balls-to-each-box
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-move-all-balls-to-each-box.py
# solution_class: Solution
# submission_id: 127956bcd3d2f6a35eb40d32d65baa735ed5fecd
# seed: 207626993

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result = [0]*len(boxes)
        for direction in (lambda x:x, reversed):
            cnt = accu = 0
            for i in direction(xrange(len(boxes))):
                result[i] += accu
                if boxes[i] == '1':
                    cnt += 1
                accu += cnt
        return result