# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-word-with-all-prefixes
# source_path: LeetCode-Solutions-master/Python/longest-word-with-all-prefixes.py
# solution_class: Solution2
# submission_id: 632ac705b7b279485e8de49def85415d9d331770
# seed: 209769371

# Time:  O(n)
# Space: O(t), t is the number of nodes in trie

import collections
import string

class Solution2(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(words, node, result):
            if result[0] == -1 or len(words[node["_end"]]) > len(words[result[0]]):
                result[0] = node["_end"]
            for c in string.ascii_lowercase:
                if c not in node or "_end" not in node[c]:
                    continue
                dfs(words, node[c], result)
    
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        trie["_end"] = -1
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)["_end"] = i
        result = [-1]
        dfs(words, trie, result)
        return words[result[0]] if result[0] != -1 else ""