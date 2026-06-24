# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: weighted-word-mapping
# source_path: LeetCode-Solutions-master/Python/weighted-word-mapping.py
# solution_class: Solution2
# submission_id: b0834bd855c223d3a9cafd69c33986c91631ff6b
# seed: 989636713

# Time:  O(n * l)
# Space: O(1)

# string

class Solution2(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        return "".join(chr(ord('z')-reduce(lambda accu, x: (accu+x)%26, map(lambda x: weights[ord(x)-ord('a')], w), 0)) for w in words)