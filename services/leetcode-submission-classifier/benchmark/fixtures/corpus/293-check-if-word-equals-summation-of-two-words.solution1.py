# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-word-equals-summation-of-two-words
# source_path: LeetCode-Solutions-master/Python/check-if-word-equals-summation-of-two-words.py
# solution_class: Solution
# submission_id: 1c76071ae72a28b533e9c0d08b3822f5807065ba
# seed: 3528987908

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def stoi(s):
            result = 0
            for c in s:
                result = result*10 + ord(c)-ord('a')
            return result
        
        return stoi(firstWord) + stoi(secondWord) == stoi(targetWord)