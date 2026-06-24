# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-nice-subarrays
# source_path: LeetCode-Solutions-master/Python/count-number-of-nice-subarrays.py
# solution_class: Solution2
# submission_id: 3cd4ba8be6d82e11c2c86427b542edf02415109e
# seed: 3628411197

# Time:  O(n)
# Space: O(k)

class Solution2(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        dq = collections.deque([-1])
        for i in xrange(len(nums)):
            if nums[i]%2:
                dq.append(i)
            if len(dq) > k+1:
                dq.popleft()
            if len(dq) == k+1:
                result += dq[1]-dq[0]
        return result