# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-words-formed-by-letters
# source_path: LeetCode-Solutions-master/Python/maximum-score-words-formed-by-letters.py
# solution_class: Solution
# submission_id: 8a701b4d7d68fec8d65832f7be4b77c60c0430a0
# seed: 4027780201

# Time:  O(n * 2^n)
# Space: O(n)

import collections

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        def backtracking(words, word_scores, word_counts, curr, curr_score, letter_count, result):
            result[0] = max(result[0], curr_score) 
            for i in xrange(curr, len(words)):
                if any(letter_count[c] < word_counts[i][c] for c in word_counts[i]):
                    continue
                backtracking(words, word_scores, word_counts, i+1,
                             curr_score+word_scores[i], letter_count-word_counts[i],
                             result)

        letter_count = collections.Counter(letters)    
        word_counts = map(collections.Counter, words)
        word_scores = [sum(score[ord(c)-ord('a')] for c in words[i])
                       for i in xrange(len(words))]
        result = [0]
        backtracking(words, word_scores, word_counts, 0, 0, letter_count, result)
        return result[0]