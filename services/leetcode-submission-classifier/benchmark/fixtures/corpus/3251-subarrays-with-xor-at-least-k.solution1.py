# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarrays-with-xor-at-least-k
# source_path: LeetCode-Solutions-master/Python/subarrays-with-xor-at-least-k.py
# solution_class: Solution
# submission_id: 4ed325b54499e35be68f0566bb21fbf5f8ddb4ac
# seed: 3717516595

# Time:  O(nlogr), r = max(max(nums), k, 1)
# Space: O(nlogr)

# bitmasks, prefix sum, trie

class Solution(object):
    def countXorSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        class Trie(object):
            def __init__(self, bit_length):
                self.__lefts = [-1]*(1+(1+len(nums))*bit_length)  # preallocate to speed up performance
                self.__rights = [-1]*(1+(1+len(nums))*bit_length)
                self.__cnts = [0]*(1+(1+len(nums))*bit_length)
                self.__i = 0
                self.__new_node()
                self.__bit_length = bit_length
            
            def __new_node(self):
                self.__i += 1
                return self.__i-1

            def add(self, num):
                curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = (num>>i)&1
                    if x == 0:
                        if self.__lefts[curr] == -1:
                            self.__lefts[curr] = self.__new_node()
                        curr = self.__lefts[curr]
                    else:
                        if self.__rights[curr] == -1:
                            self.__rights[curr] = self.__new_node()
                        curr = self.__rights[curr]
                    self.__cnts[curr] += 1
                        
            def query(self, prefix, k):
                result = curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    t = (k>>i)&1
                    x = (prefix>>i)&1
                    if t == 0:
                        tmp = self.__lefts[curr] if 1^x == 0 else self.__rights[curr]
                        if tmp != -1:
                            result += self.__cnts[tmp]
                    curr = self.__lefts[curr] if t^x == 0 else self.__rights[curr]
                    if curr == -1:
                        break
                else:
                    result += self.__cnts[curr]
                return result
    
        result = prefix = 0
        mx = max(max(nums), k, 1)
        trie = Trie(mx.bit_length())
        trie.add(prefix)
        for x in nums:
            prefix ^= x
            result += trie.query(prefix, k)
            trie.add(prefix)
        return result