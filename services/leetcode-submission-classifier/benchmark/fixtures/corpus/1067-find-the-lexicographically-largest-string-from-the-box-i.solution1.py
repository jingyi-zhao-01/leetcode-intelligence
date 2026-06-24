# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-lexicographically-largest-string-from-the-box-i
# source_path: LeetCode-Solutions-master/Python/find-the-lexicographically-largest-string-from-the-box-i.py
# solution_class: Solution
# submission_id: 2b42b48654f9195b63e1040b208ac40f2dbf2c88
# seed: 3953126618

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        idx = l = 0
        for i in xrange(1, len(word)):
            if word[i] == word[idx+l]:
                l += 1
            elif word[i] < word[idx+l]:
                l = 0
            elif word[i] > word[idx+l]:
                if word[i-l] >= word[i]:
                    idx = i-l
                else:
                    idx = i
                l = 0
        return word[idx:len(word)-max((numFriends-1)-idx, 0)]