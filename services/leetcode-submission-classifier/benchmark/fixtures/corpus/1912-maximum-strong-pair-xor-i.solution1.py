# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strong-pair-xor-i
# source_path: LeetCode-Solutions-master/Python/maximum-strong-pair-xor-i.py
# solution_class: Solution
# submission_id: fbaac1e06bf194c8cfbd4fc9dbbb6ffc7ba59467
# seed: 2767157090

# Time:  O(nlogn + nlogr) = O(nlogr), r = max(nums)
# Space: O(t)

# bit manipulation, greedy, trie, sort, two pointers

class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class Trie(object):
            def __init__(self, bit_length):
                self.__nodes = []
                self.__cnts = []
                self.__new_node()
                self.__bit_length = bit_length
            
            def __new_node(self):
                self.__nodes.append([-1]*2)
                self.__cnts.append(0)
                return len(self.__nodes)-1

            def update(self, num, d):
                curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = num>>i
                    if self.__nodes[curr][x&1] == -1:
                        self.__nodes[curr][x&1] = self.__new_node()
                    curr = self.__nodes[curr][x&1]
                    self.__cnts[curr] += d
                        
            def query(self, num):
                result = curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    result <<= 1
                    x = num>>i
                    if self.__nodes[curr][1^(x&1)] != -1 and self.__cnts[self.__nodes[curr][1^(x&1)]]:
                        curr = self.__nodes[curr][1^(x&1)]
                        result |= 1
                    else:
                        curr = self.__nodes[curr][x&1]
                return result
    
        nums.sort()
        trie = Trie(nums[-1].bit_length())
        result = j = 0
        for i, num in enumerate(nums):
            trie.update(num, +1)
            while not (nums[i] <= 2*nums[j]) :
                trie.update(nums[j], -1)
                j += 1
            result = max(result, trie.query(num))
        return result