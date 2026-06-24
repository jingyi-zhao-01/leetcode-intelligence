# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-sub-folders-from-the-filesystem
# source_path: LeetCode-Solutions-master/Python/remove-sub-folders-from-the-filesystem.py
# solution_class: Solution
# submission_id: 33166dceb68af1edb893264a8a948186f9a980ec
# seed: 3382462907

# Time:  O(n), n is the total sum of the lengths of folder names
# Space: O(t), t is the number of nodes in trie

import collections
import itertools

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        def dfs(curr, path, result):
            if "_end" in curr:
                result.append("/" + "/".join(path))
                return
            for c in curr:
                if c == "_end":
                    continue
                path.append(c)
                dfs(curr[c], path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for f in folder:
            f_list = f.split("/")
            reduce(dict.__getitem__,
                   itertools.islice(f_list, 1, len(f_list)),
                   trie).setdefault("_end")
        result = []
        dfs(trie, [], result)
        return result