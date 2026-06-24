# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-xor-with-bounded-range
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-xor-with-bounded-range.py
# solution_class: Solution3
# submission_id: aa73e82c103be78547dfd95eb0607194a17f1e43
# seed: 1971077247

# Time:  O(nlogr), r = max(max(nums), 1)
# Space: O(n)

import collections


# two pointers, mono deque, bitmasks, prefix sum, hash table

class Solution3(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
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

            def add(self, num, diff):
                curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = (num>>i)&1
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
                    self.__cnts[curr] += diff
                        
            def query(self, prefix):
                result = curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = (prefix>>i)&1
                    if self.__nodes[curr][x^1] != -1 and self.__cnts[self.__nodes[curr][x^1]]:
                        result |= 1<<i
                        curr = self.__nodes[curr][x^1]
                    else:
                        curr = self.__nodes[curr][x]
                return result
    
        result = 0
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]^nums[i]
        mx = max(max(nums), 1)
        trie = Trie(mx.bit_length())
        trie.add(prefix[0], +1)
        max_dq = collections.deque()
        min_dq = collections.deque()
        left = 0
        for right in xrange(len(nums)):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            while nums[max_dq[0]]-nums[min_dq[0]] > k:
                trie.add(prefix[left], -1)
                if max_dq and max_dq[0] == left:
                    max_dq.popleft()
                if min_dq and min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            result = max(result, trie.query(prefix[right+1]))
            trie.add(prefix[right+1], +1)
        return result