# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-in-zigzag-labelled-binary-tree
# source_path: LeetCode-Solutions-master/Python/path-in-zigzag-labelled-binary-tree.py
# solution_class: Solution
# submission_id: 83d9b9d726f020e5f39eae54af4f676ef1ca461b
# seed: 1367193065

# Time:  O(logn)
# Space: O(logn)

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        count = 2**label.bit_length()
        result = []
        while label >= 1:
            result.append(label)
            label = ((count//2) + ((count-1)-label)) // 2
            count //= 2
        result.reverse()
        return result