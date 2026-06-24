# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-of-two-numbers-in-an-array
# source_path: LeetCode-Solutions-master/Python/maximum-xor-of-two-numbers-in-an-array.py
# solution_class: Solution
# submission_id: bf46c0f0e2ef8b74dfc07560573cd8437c5656eb
# seed: 862299750

# Time:  O(nlogr), r = max(nums)
# Space: O(t)

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class Trie(object):
            def __init__(self, bit_length):
                self.__nodes = []
                self.__new_node()
                self.__bit_length = bit_length
            
            def __new_node(self):
                self.__nodes.append([-1]*2)
                return len(self.__nodes)-1

            def insert(self, num):
                curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = num>>i
                    if self.__nodes[curr][x&1] == -1:
                        self.__nodes[curr][x&1] = self.__new_node()
                    curr = self.__nodes[curr][x&1]
                        
            def query(self, num):
                result = curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    result <<= 1
                    x = num>>i
                    if self.__nodes[curr][1^(x&1)] != -1:
                        curr = self.__nodes[curr][1^(x&1)]
                        result |= 1
                    else:
                        curr = self.__nodes[curr][x&1]
                return result

        trie = Trie(max(nums).bit_length())
        result = 0
        for num in nums:
            trie.insert(num)
            result = max(result, trie.query(num))
        return result