# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-string-into-substrings-with-values-at-most-k
# source_path: LeetCode-Solutions-master/Python/partition-string-into-substrings-with-values-at-most-k.py
# solution_class: Solution
# submission_id: 5327ba8cbc299953382d2eb23c94496dd264303d
# seed: 1321190079

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 1
        curr = 0
        for c in s:
            if int(c) > k:
                return -1
            if curr*10+int(c) > k:
                result += 1
                curr = 0
            curr = curr*10+int(c)
        return result