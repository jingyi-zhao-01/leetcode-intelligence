# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenated-words
# source_path: LeetCode-Solutions-master/Python/concatenated-words.py
# solution_class: Solution
# submission_id: b760e4d3200711044d6264dc32f051864b97a366
# seed: 755383054

# Time:  O(n * l^2)
# Space: O(n * l)

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = set(words)
        result = []
        for word in words:
            dp = [False] * (len(word)+1)
            dp[0] = True
            for i in xrange(len(word)):
                if not dp[i]:
                    continue

                for j in xrange(i+1, len(word)+1):
                    if j - i < len(word) and word[i:j] in lookup:
                        dp[j] = True

                if dp[len(word)]:
                    result.append(word)
                    break

        return result