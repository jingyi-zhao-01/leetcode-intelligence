# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-sentence-is-pangram
# source_path: LeetCode-Solutions-master/Python/check-if-the-sentence-is-pangram.py
# solution_class: Solution
# submission_id: e5bd30c0a488d5823560a3afa3b94089dfd380d5
# seed: 1221193527

# Time:  O(n)
# Space: O(26) = O(1)

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26