# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ransom-note
# source_path: LeetCode-Solutions-master/Python/ransom-note.py
# solution_class: Solution
# submission_id: cbf79b13b7c143eb0f21dd7860bbac53743ce5ed
# seed: 2303918009

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] * 26
        letters = 0

        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1

        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break

        return letters == 0