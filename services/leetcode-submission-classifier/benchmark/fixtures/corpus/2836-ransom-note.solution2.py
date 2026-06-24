# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ransom-note
# source_path: LeetCode-Solutions-master/Python/ransom-note.py
# solution_class: Solution2
# submission_id: 7354e8802d354c168d431df6f23abcb2a5aef19d
# seed: 3314116474

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)