# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: map-sum-pairs
# source_path: LeetCode-Solutions-master/Python/map-sum-pairs.py
# solution_class: Solution
# submission_id: 37ba52af72f235d8f575c6786c453e80a77e006f
# seed: 2399612437

# Time:  O(n), n is the length of key
# Space: O(t), t is the number of nodes in trie

import collections


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__root = _trie()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # Time: O(n)
        curr = self.__root
        for c in key:
            curr = curr[c]
        delta = val
        if "_end" in curr:
            delta -= curr["_end"]

        curr = self.__root
        for c in key:
            curr = curr[c]
            if "_count" in curr:
                curr["_count"] += delta
            else:
                curr["_count"] = delta
        curr["_end"] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # Time: O(n)
        curr = self.__root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr["_count"]



