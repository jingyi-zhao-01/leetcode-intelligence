# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-that-match-a-pattern-i
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-that-match-a-pattern-i.py
# solution_class: Solution2
# submission_id: 225f1eba27f9500718ea2923917cf72b607c5516
# seed: 2552044882

# Time:  O(n)
# Space: O(m)

# kmp

class Solution2(object):
    def countMatchingSubarrays(self, nums, pattern):
        """
        :type nums: List[int]
        :type pattern: List[int]
        :rtype: int
        """
        def check(i):
            return all(nums[i+j] == pattern[j] for j in xrange(len(pattern)))
    
        for i in xrange(len(nums)-1):
            nums[i] = cmp(nums[i+1], nums[i])
        return sum(check(i) for i in xrange(len(nums)-len(pattern)+1))