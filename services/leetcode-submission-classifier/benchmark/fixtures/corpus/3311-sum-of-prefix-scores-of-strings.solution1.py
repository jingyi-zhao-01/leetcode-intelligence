# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-prefix-scores-of-strings
# source_path: LeetCode-Solutions-master/Python/sum-of-prefix-scores-of-strings.py
# solution_class: Solution
# submission_id: ff29165a57f76589a33ebd77e91283b4488bde5b
# seed: 2378354012

# Time:  O(n * l), n is the number of words, l is the max length of words
# Space: O(t), t is the size of trie
    
import collections


# trie

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for w in words:
            curr = trie
            for c in w:
                curr = curr[c]
                curr["_cnt"] = curr["_cnt"]+1 if "_cnt" in curr else 1
        result = []
        for w in words:
            cnt = 0
            curr = trie
            for c in w:
                curr = curr[c]
                cnt += curr["_cnt"]
            result.append(cnt)
        return result