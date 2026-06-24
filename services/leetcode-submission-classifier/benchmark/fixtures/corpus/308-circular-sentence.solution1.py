# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: circular-sentence
# source_path: LeetCode-Solutions-master/Python/circular-sentence.py
# solution_class: Solution
# submission_id: 1b924cd3d5a055e8844b358616eebed9d0b4f671
# seed: 1852773552

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return sentence[0] == sentence[-1] and all(sentence[i-1] == sentence[i+1]for i in xrange(len(sentence)) if sentence[i] == ' ')