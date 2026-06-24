# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-word-in-dictionary
# source_path: LeetCode-Solutions-master/Python/longest-word-in-dictionary.py
# solution_class: Solution
# submission_id: 3a18cfa22713e47572b7329ff123738b15aeac63
# seed: 2716347706

# Time:  O(n), n is the total sum of the lengths of words
# Space: O(t), t is the number of nodes in trie

from collections import defaultdict
from operator import getitem

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        _trie = lambda: defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            reduce(getitem, word, trie)["_end"] = i

        # DFS
        stack = trie.values()
        result = ""
        while stack:
            curr = stack.pop()
            if "_end" in curr:
                word = words[curr["_end"]]
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
                stack += [curr[letter] for letter in curr if letter != "_end"]
        return result