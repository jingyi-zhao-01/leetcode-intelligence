# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: patching-array
# source_path: LeetCode-Solutions-master/Python/patching-array.py
# solution_class: Solution2
# submission_id: 61cf2f18fb89365946656fa59b1927acab3f572f
# seed: 3108027408

# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)

class Solution2(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        result = reachable = 0
        for x in nums:
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
                if reachable >= n:
                    return result
            reachable += x
            if reachable >= n:
                return result
        while not reachable >= n:
            result += 1
            reachable += reachable+1
        return result