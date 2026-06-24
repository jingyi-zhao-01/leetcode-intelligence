# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-xor-with-bounded-range
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-xor-with-bounded-range.py
# solution_class: Solution2
# submission_id: 20302cf593c2bd2c912d5a1a78385760baed039c
# seed: 39262862

# Time:  O(nlogr), r = max(max(nums), 1)
# Space: O(n)

import collections


# two pointers, mono deque, bitmasks, prefix sum, hash table

class Solution2(object):
    def maxXor(self, nums, k):
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

            def add(self, num, diff):
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
                    self.__cnts[curr] += diff
                        
            def query(self, prefix):
                result = curr = 0
                for i in reversed(xrange(self.__bit_length)):
                    x = (prefix>>i)&1
                    l, r = (self.__lefts, self.__rights) if x^1 else (self.__rights, self.__lefts)
                    if r[curr] != -1 and self.__cnts[r[curr]]:
                        result |= 1<<i
                        curr = r[curr]
                    else:
                        curr = l[curr]
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