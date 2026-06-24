# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: uncommon-words-from-two-sentences
# source_path: LeetCode-Solutions-master/Python/uncommon-words-from-two-sentences.py
# solution_class: Solution
# submission_id: e4ce17d44384142436d250d55c2780ac128c6512
# seed: 459974045

# Time:  O(m + n)
# Space: O(m + n)

import collections

    

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [word for word in count if count[word] == 1]