# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: query-kth-smallest-trimmed-number
# source_path: LeetCode-Solutions-master/Python/query-kth-smallest-trimmed-number.py
# solution_class: Solution2
# submission_id: c990d2fa52924718bdc7222c741e536965c1f6d8
# seed: 2183879424

# Time:  O(q + n * t)
# Space: O(t + n + q)

# radix sort

class Solution2(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
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

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def compare(a, b):
            for i in xrange(len(nums[a])-t, len(nums[a])):
                if nums[a][i] < nums[b][i]:
                    return True
                if nums[a][i] > nums[b][i]:
                    return False
            return cmp(a, b) < 0

        result = []
        idxs = range(len(nums))
        for k, t in queries:
            nth_element(idxs, k-1, compare=compare)
            result.append(idxs[k-1])
        return result