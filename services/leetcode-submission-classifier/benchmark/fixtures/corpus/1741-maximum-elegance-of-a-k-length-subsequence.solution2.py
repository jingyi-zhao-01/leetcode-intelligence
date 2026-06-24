# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-elegance-of-a-k-length-subsequence
# source_path: LeetCode-Solutions-master/Python/maximum-elegance-of-a-k-length-subsequence.py
# solution_class: Solution2
# submission_id: b4b386c850f976f5847a351b01e4b8d6d20ea05e
# seed: 2314436461

# Time:  O(nlogk)
# Space: O(k)

import heapq
from sortedcontainers import SortedList


# heap, sorted list, greedy

class Solution2(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, left=0, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right
            
            right = len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1
    
        def nlargest(k, nums):
            nth_element(nums, k-1, compare=lambda a, b: a > b)
            return sorted(nums[:k], reverse=True)
    
        curr = 0
        lookup = set()
        stk = []
        for p, c in nlargest(k, items):
            if c in lookup:
                stk.append(p)
            curr += p
            lookup.add(c)
        lookup2 = collections.defaultdict(int)
        for p, c in items:
            if c in lookup:
                continue
            lookup2[c] = max(lookup2[c], p)
        l = len(lookup)
        result = curr+l**2
        for p in nlargest(min(len(stk), len(lookup2)), lookup2.values()):
            curr += p-stk.pop()
            l += 1
            result = max(result, curr+l**2) 
        return result