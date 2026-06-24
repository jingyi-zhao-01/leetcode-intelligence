# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-pair-removal-to-sort-array-i
# source_path: LeetCode-Solutions-master/Python/minimum-pair-removal-to-sort-array-i.py
# solution_class: Solution
# submission_id: 5c47af93d03de2db04a5a58718e34241c97de787
# seed: 1150611545

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# simulation, doubly linked list, sorted list

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def add(i):
            if 0 <= i < right[i] < len(nums):
                sl.add([nums[i]+nums[right[i]], i])
                if nums[i] > nums[right[i]]:
                    cnt[0] += 1

        def remove(i):
            if 0 <= i < right[i] < len(nums):
                sl.remove([nums[i]+nums[right[i]], i])
                if nums[i] > nums[right[i]]:
                    cnt[0] -= 1

        left = range(-1, (len(nums)+1)-1)
        right = range(1, len(nums)+1)
        cnt = [sum(nums[i] > nums[i+1] for i in xrange(len(nums)-1))]
        sl = SortedList([nums[i]+nums[i+1], i] for i in xrange(len(nums)-1))
        result = 0
        while cnt[0]:
            _, i = sl[0]
            remove(left[i])
            remove(i)
            remove(right[i])
            nums[i] += nums[right[i]]
            left[right[right[i]]] = i
            right[i] = right[right[i]]
            add(left[i])
            add(i)
            result += 1
        return result