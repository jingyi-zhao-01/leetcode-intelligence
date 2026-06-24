# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
# source_path: LeetCode-Solutions-master/Python/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence.py
# solution_class: Solution
# submission_id: 8d2c33453e1bc70e415d2c323aa8b94e29006b81
# seed: 1371199408

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        def KMP(text, pattern):
            def getPrefix(pattern):
                prefix = [-1] * len(pattern)
                j = -1
                for i in xrange(1, len(pattern)):
                    while j > -1 and pattern[j + 1] != pattern[i]:
                        j = prefix[j]
                    if pattern[j + 1] == pattern[i]:
                        j += 1
                    prefix[i] = j
                return prefix
    
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(len(text)):
                while j != -1 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    return i-j
            return -1
        
        if sentence.startswith(searchWord):
            return 1
        p = KMP(sentence, ' ' + searchWord)
        if p == -1:
            return -1
        return 1+sum(sentence[i] == ' ' for i in xrange(p+1))