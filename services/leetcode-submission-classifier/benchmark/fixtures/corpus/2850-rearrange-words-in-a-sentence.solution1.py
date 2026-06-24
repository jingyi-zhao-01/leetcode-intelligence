# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-words-in-a-sentence
# source_path: LeetCode-Solutions-master/Python/rearrange-words-in-a-sentence.py
# solution_class: Solution
# submission_id: c69599cb4bc0003c3a26701a88f4a808b39afcec
# seed: 2010131433

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        result = text.split()
        result[0] = result[0].lower()
        result.sort(key=len) 
        result[0] = result[0].title()
        return " ".join(result)