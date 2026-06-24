# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: weighted-word-mapping
# source_path: LeetCode-Solutions-master/Python/weighted-word-mapping.py
# solution_class: Solution
# submission_id: 4b8b1c5664bf51e5d3895bb327fa05507db6aa24
# seed: 3641915399

# Time:  O(n * l)
# Space: O(1)

# string

class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        for w in words:
            i = 0
            for x in w:
                i = (i+weights[ord(x)-ord('a')])%26
            result.append(chr(ord('z')-i))
        return "".join(result)