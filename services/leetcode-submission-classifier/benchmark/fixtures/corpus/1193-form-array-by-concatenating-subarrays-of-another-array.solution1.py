# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: form-array-by-concatenating-subarrays-of-another-array
# source_path: LeetCode-Solutions-master/Python/form-array-by-concatenating-subarrays-of-another-array.py
# solution_class: Solution
# submission_id: 303a839ba13047beb71251f9096629f22c6e7d75
# seed: 3656351333

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        
        def KMP(text, pattern, start):
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(start, len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    return i-j
            return -1

        pos = 0
        for group in groups:
            pos = KMP(nums, group, pos)
            if pos == -1:
                return False
            pos += len(group)
        return True