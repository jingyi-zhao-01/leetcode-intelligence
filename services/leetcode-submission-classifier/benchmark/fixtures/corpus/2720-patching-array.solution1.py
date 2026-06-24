# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: patching-array
# source_path: LeetCode-Solutions-master/Python/patching-array.py
# solution_class: Solution
# submission_id: a9bc4bc49993a91084ff5d169b7fff0fd8c06b52
# seed: 3330903766

# Time:  O(s + logn), s is the number of elements in the array
# Space: O(1)

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        result = reachable = 0
        for x in nums:
            if x > n:
                break
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
            reachable += x
        while not reachable >= n:
            result += 1
            reachable += reachable+1
        return result