# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-weakest-rows-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/the-k-weakest-rows-in-a-matrix.py
# solution_class: Solution3
# submission_id: 6c4cc7e067ba8097718008c0335f2efbee8f84d9
# seed: 252605462

# Time:  O(m * n)
# Space: O(k)

class Solution3(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def partition_around_pivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = partition_around_pivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == n:
                    return
                elif new_pivot_idx > n:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < n
                    left = new_pivot_idx + 1
        
        nums = [(sum(mat[i]), i) for i in xrange(len(mat))]
        nth_element(nums, k)
        return map(lambda x: x[1], sorted(nums[:k]))