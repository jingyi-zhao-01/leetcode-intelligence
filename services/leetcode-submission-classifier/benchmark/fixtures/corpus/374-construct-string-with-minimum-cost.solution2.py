# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-string-with-minimum-cost
# source_path: LeetCode-Solutions-master/Python/construct-string-with-minimum-cost.py
# solution_class: Solution2
# submission_id: d369c167bab9765516014dfa96be1ad2e56861d3
# seed: 1834148560

# Time:  O(n^2 + w * l)
# Space: O(t)

import itertools


# trie, dp

class Solution2(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        INF = float("inf")
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__mns = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                self.__mns.append(INF)
                return len(self.__nodes)-1

            def add(self, w, c):
                curr = 0
                for x in w:
                    x = ord(x)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
                self.__mns[curr] = min(self.__mns[curr], c)
            
            def query(self, i):
                curr = 0
                for j in xrange(i, len(target)):
                    x = ord(target[j])-ord('a')
                    if self.__nodes[curr][x] == -1:
                        break
                    curr = self.__nodes[curr][x]
                    if self.__mns[curr] != INF:
                        dp[j+1] = min(dp[j+1], dp[i]+self.__mns[curr])
    
        trie = Trie()
        for w, c in itertools.izip(words, costs):
            trie.add(w, c)
        dp = [INF]*(len(target)+1)
        dp[0] = 0
        for i in xrange(len(target)):
            if dp[i] == INF:
                continue
            trie.query(i)
        return dp[-1] if dp[-1] != INF else -1