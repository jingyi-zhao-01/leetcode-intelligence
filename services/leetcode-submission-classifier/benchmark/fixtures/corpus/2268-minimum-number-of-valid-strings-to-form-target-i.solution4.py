# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-valid-strings-to-form-target-i
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-valid-strings-to-form-target-i.py
# solution_class: Solution4
# submission_id: 756caba0198e9edd0dbbbdf29eec04d0382ceb07
# seed: 3833956655

# Time:  O(n + w * l)
# Space: O(n + w * l)

# rolling hash, hash table, two pointers, sliding window, dp

class Solution4(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                return len(self.__nodes)-1

            def add(self, w):
                curr = 0
                for c in w:
                    x = ord(c)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
            
            def query(self, target, i):
                curr = 0
                for l in xrange(len(target)-i):
                    x = ord(target[i+l])-ord('a')
                    if self.__nodes[curr][x] == -1:
                        return l
                    curr = self.__nodes[curr][x]
                return len(target)-i

        trie = Trie()
        for w in words:
            trie.add(w)
        lookup = [0]*len(target)
        for i in xrange(len(target)):
            l = trie.query(target, i)
            for nl in xrange(1, l+1):
                lookup[i+nl-1] = max(lookup[i+nl-1], nl)
        dp = [0]*(len(target)+1)
        for i in xrange(len(target)):
            if not lookup[i]:
                return -1
            dp[i+1] = dp[(i-lookup[i])+1]+1
        return dp[-1]