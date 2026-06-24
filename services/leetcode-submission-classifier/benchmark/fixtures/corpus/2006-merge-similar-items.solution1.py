# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-similar-items
# source_path: LeetCode-Solutions-master/Python/merge-similar-items.py
# solution_class: Solution
# submission_id: 3abef6578f7488693732f8f05fbb037f4ad9bcd6
# seed: 844030843

# Time:  O((m + n) * log(m + n))
# Space: O(m + n)

# freq table, sort

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        return sorted((Counter(dict(items1))+Counter(dict(items2))).iteritems())