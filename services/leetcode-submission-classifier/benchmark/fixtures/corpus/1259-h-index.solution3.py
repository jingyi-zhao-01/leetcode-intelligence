# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: h-index
# source_path: LeetCode-Solutions-master/Python/h-index.py
# solution_class: Solution3
# submission_id: 927f0c721c5d941a982ca3079640978473650bdc
# seed: 4260416408

# Time:  O(n)
# Space: O(n)

class Solution3(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(x >= i + 1 for i, x in enumerate(sorted(citations, reverse=True)))