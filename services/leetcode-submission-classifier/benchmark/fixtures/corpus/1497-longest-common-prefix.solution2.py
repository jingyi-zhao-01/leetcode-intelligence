# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-prefix
# source_path: LeetCode-Solutions-master/Python/longest-common-prefix.py
# solution_class: Solution2
# submission_id: 9e4386bc06ad145e26bdb221cc37ad4a8aa694c4
# seed: 4184093420

# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix
            
        return prefix