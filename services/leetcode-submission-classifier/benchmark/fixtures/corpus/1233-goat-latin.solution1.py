# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: goat-latin
# source_path: LeetCode-Solutions-master/Python/goat-latin.py
# solution_class: Solution
# submission_id: 759ffabfd69a0f7eeb79a5c2a5b98642117a701f
# seed: 800923957

# Time:  O(n + w^2), n = w * l,
#                    n is the length of S,
#                    w is the number of word,
#                    l is the average length of word
# Space: O(n)

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def convert(S):
            vowel = set('aeiouAEIOU')
            for i, word in enumerate(S.split(), 1):
                if word[0] not in vowel:
                    word = word[1:] + word[:1]
                yield word + 'ma' + 'a'*i
        return " ".join(convert(S))