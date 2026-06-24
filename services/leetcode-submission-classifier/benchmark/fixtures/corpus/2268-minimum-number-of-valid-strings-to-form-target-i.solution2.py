# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-valid-strings-to-form-target-i
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-valid-strings-to-form-target-i.py
# solution_class: Solution2
# submission_id: f20c44d3282e31c165b936804866bf169b694f46
# seed: 643940830

# Time:  O(n + w * l)
# Space: O(n + w * l)

# rolling hash, hash table, two pointers, sliding window, dp

class Solution2(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        trie = AhoTrie(words)
        dp = [0]*(len(target)+1)
        for i in xrange(len(target)):
            l = trie.step(target[i])
            if not l:
                return -1
            dp[i+1] = dp[(i-l)+1]+1
        return dp[-1]