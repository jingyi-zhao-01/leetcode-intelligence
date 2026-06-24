# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-with-majority-element-ii
# source_path: LeetCode-Solutions-master/Python/count-subarrays-with-majority-element-ii.py
# solution_class: Solution
# submission_id: 3b9a0ab1292ecb653f1434d7d252a19ff4910288
# seed: 2576343910

# Time:  O(n)
# Space: O(n)

# prefix sum, freq table

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = [0]*((2*len(nums)+1)+1)
        prefix = [0]*((2*len(nums)+1)+1)
        prefix[0] = cnt[0] = 1
        result = curr = 0
        for x in nums:
            curr += +1 if x == target else -1
            cnt[curr] += 1
            prefix[curr] = prefix[curr-1]+cnt[curr]
            result += prefix[curr-1]
        return result