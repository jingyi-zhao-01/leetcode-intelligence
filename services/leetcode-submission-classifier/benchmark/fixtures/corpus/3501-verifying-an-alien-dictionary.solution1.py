# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: verifying-an-alien-dictionary
# source_path: LeetCode-Solutions-master/Python/verifying-an-alien-dictionary.py
# solution_class: Solution
# submission_id: 9fd8a4ef9649415c5733594d04faac586c6ee5bc
# seed: 1279357858

# Time:  O(n * l), l is the average length of words
# Space: O(1)

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        lookup = {c: i for i, c in enumerate(order)}
        for i in xrange(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for k in xrange(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if lookup[word1[k]] > lookup[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True