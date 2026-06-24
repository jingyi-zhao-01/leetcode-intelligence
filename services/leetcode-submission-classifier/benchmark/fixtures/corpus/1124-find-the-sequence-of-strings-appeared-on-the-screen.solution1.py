# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-sequence-of-strings-appeared-on-the-screen
# source_path: LeetCode-Solutions-master/Python/find-the-sequence-of-strings-appeared-on-the-screen.py
# solution_class: Solution
# submission_id: 0c7cb082094929d3201553a206148010379f54fd
# seed: 5027906

# Time:  O(n^2)
# Space: O(1)

# string

class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        return [target[:i]+chr(x) for i in xrange(len(target)) for x in xrange(ord('a'), ord(target[i])+1)]