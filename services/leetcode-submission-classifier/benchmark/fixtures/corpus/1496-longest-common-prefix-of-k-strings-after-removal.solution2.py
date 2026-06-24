# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-prefix-of-k-strings-after-removal
# source_path: LeetCode-Solutions-master/Python/longest-common-prefix-of-k-strings-after-removal.py
# solution_class: Solution2
# submission_id: dacb34576e3ed0386f4ade243bd27a23f0524c76
# seed: 2485934270

# Time:  O(l * nlogn)
# Space: O(n)

# sort, sliding window, prefix sum

class Solution2(object):
    def longestCommonPrefix(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[int]
        """
        class Trie(object):
            def __init__(self):
                self.__root = self.__new_node()
            
            def __new_node(self):
                return {"cnt":0, "max":0}

            def update(self, w, d, k):
                path = [None]*(len(w)+1)
                path[0] = curr = self.__root
                for i, x in enumerate(w, 1):
                    if x not in curr:
                        curr[x] = self.__new_node()
                    path[i] = curr = curr[x]
                for i in reversed(xrange(len(path))):
                    curr = path[i]
                    curr["cnt"] += d
                    curr["max"] = i if curr["cnt"] >= k else 0
                    for x in curr.iterkeys():
                        if len(x) == 1:
                            curr["max"] = max(curr["max"], curr[x]["max"])

            def query(self):
                return self.__root["max"]
        

        trie = Trie()
        for w in words:
            trie.update(w, +1, k)
        result = [0]*len(words)
        for i in xrange(len(words)):
            trie.update(words[i], -1, k)
            result[i] = trie.query()
            trie.update(words[i], +1, k)
        return result