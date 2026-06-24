# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-tag-for-video-caption
# source_path: LeetCode-Solutions-master/Python/generate-tag-for-video-caption.py
# solution_class: Solution2
# submission_id: fbb5bc90de791aa1dcc5713b91710c9bd777a692
# seed: 1443959042

# Time:  O(n)
# Space: O(1)

# string

class Solution2(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        L = 100
        return ('#'+"".join(x.lower() if i == 0 else x[0].upper()+x[1:].lower() for i, x in enumerate(caption.split())))[:L]