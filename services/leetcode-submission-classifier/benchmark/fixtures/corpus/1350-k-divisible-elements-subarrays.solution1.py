# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-divisible-elements-subarrays
# source_path: LeetCode-Solutions-master/Python/k-divisible-elements-subarrays.py
# solution_class: Solution
# submission_id: 9cc9f5af3f9a8ded3c4b96c86947a414ed400b3d
# seed: 3095529930

# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# trie

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for i in xrange(len(nums)):
            cnt = 0
            curr = trie
            for j in xrange(i, len(nums)):
                cnt += (nums[j]%p == 0)
                if cnt > k:
                    break
                if nums[j] not in curr:
                    result += 1
                curr = curr[nums[j]]
        return result