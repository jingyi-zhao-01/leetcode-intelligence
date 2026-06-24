# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: making-file-names-unique
# source_path: LeetCode-Solutions-master/Python/making-file-names-unique.py
# solution_class: Solution
# submission_id: fd99564c5c0e51445f95cf7a5e41e4e2526e664e
# seed: 3408529640

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        result, lookup = [], set()
        for name in names:
            while True:
                name_with_suffix = "{}({})".format(name, count[name]) if count[name] else name
                count[name] += 1
                if name_with_suffix not in lookup:
                    break
            result.append(name_with_suffix)
            lookup.add(name_with_suffix)
        return result