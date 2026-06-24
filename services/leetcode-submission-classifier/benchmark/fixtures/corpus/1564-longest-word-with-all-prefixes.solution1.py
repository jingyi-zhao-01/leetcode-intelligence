# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-word-with-all-prefixes
# source_path: LeetCode-Solutions-master/Python/longest-word-with-all-prefixes.py
# solution_class: Solution
# submission_id: 330f919851e142bbd68e5f4fcdfdf18354a00d1b
# seed: 2028594111

# Time:  O(n)
# Space: O(t), t is the number of nodes in trie

import collections
import string

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def iter_dfs(words, node):
            result = -1
            stk = [node]
            while stk:
                node = stk.pop()
                if result == -1 or len(words[node["_end"]]) > len(words[result]):
                    result = node["_end"]
                for c in reversed(string.ascii_lowercase):
                    if c not in node or "_end" not in node[c]:
                        continue
                    stk.append(node[c])
            return result       
    
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        trie["_end"] = -1
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)["_end"] = i
        result = iter_dfs(words, trie)
        return words[result] if result != -1 else "" 