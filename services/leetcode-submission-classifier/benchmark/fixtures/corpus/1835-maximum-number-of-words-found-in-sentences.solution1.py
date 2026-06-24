# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-words-found-in-sentences
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-words-found-in-sentences.py
# solution_class: Solution
# submission_id: e28fc2a5f9221688c9a4cf3e30f5f8225c215958
# seed: 3881970681

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return 1+max(s.count(' ') for s in sentences)