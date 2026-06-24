# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotating-the-box
# source_path: LeetCode-Solutions-master/Python/rotating-the-box.py
# solution_class: Solution
# submission_id: 347d131cac01a8a8170e170112f7887b50358215
# seed: 3559339941

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        result = [['.']*len(box) for _ in xrange(len(box[0]))]
        for i in xrange(len(box)):
            k = len(box[0])-1
            for j in reversed(xrange(len(box[0]))):
                if box[i][j] == '.':
                    continue
                if box[i][j] == '*':
                    k = j
                result[k][-1-i] = box[i][j]
                k -= 1
        return result