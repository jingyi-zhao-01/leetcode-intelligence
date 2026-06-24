# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-with-xor-in-a-range
# source_path: LeetCode-Solutions-master/Python/count-pairs-with-xor-in-a-range.py
# solution_class: Solution2
# submission_id: dd04f821f50a3f43ce7c38d276ca0194283ea4ec
# seed: 2612773427

# Time:  O(n)
# Space: O(n)

import collections


# dp solution

class Solution2(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        result = 0
        trie = Trie()
        for x in nums:
            result += trie.query(x, high+1)-trie.query(x, low)
            trie.insert(x)
        return result