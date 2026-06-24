# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-lexicographically-largest-string-from-the-box-i
# source_path: LeetCode-Solutions-master/Python/find-the-lexicographically-largest-string-from-the-box-i.py
# solution_class: Solution2
# submission_id: 9499d49c3394d9936e85f385a311db9f822fcd47
# seed: 171003647

# Time:  O(n)
# Space: O(1)

# greedy

class Solution2(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        m = len(word)-(numFriends-1)
        c = max(word)
        return max(word[i:i+m] for i in xrange(len(word)) if word[i] == c)