# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-tag-for-video-caption
# source_path: LeetCode-Solutions-master/Python/generate-tag-for-video-caption.py
# solution_class: Solution
# submission_id: 36680e6ac9aa28a09254448a84b8e411e908246c
# seed: 1094566845

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        L = 100
        result = ['#']
        for i in xrange(len(caption)):
            if caption[i] == ' ':
                continue
            result.append(caption[i].upper() if i == 0 or caption[i-1] == ' ' else caption[i].lower())
            if len(result) == L:
                break
        if 1 < len(result):
            result[1] = result[1].lower()
        return "".join(result)