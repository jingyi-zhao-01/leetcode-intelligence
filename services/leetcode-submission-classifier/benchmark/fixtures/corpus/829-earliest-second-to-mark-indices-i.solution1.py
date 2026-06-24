# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: earliest-second-to-mark-indices-i
# source_path: LeetCode-Solutions-master/Python/earliest-second-to-mark-indices-i.py
# solution_class: Solution
# submission_id: b2ef2eb3af530ef59af02817b8fc92e9c4251895
# seed: 1578303107

# Time:  O(mlogm)
# Space: O(n)

# binary search, greedy

class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        def check(t):
            lookup = [-1]*len(nums)
            for i in xrange(t):
                lookup[changeIndices[i]-1] = i
            if -1 in lookup:
                return False
            cnt = 0
            for i in xrange(t):
                if i != lookup[changeIndices[i]-1]:
                    cnt += 1
                    continue
                cnt -= nums[changeIndices[i]-1]
                if cnt < 0:
                    return False
            return True

        left, right = sum(nums)+len(nums), len(changeIndices) 
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left if left <= len(changeIndices) else -1