# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-array
# source_path: LeetCode-Solutions-master/Python/rotate-array.py
# solution_class: Solution5
# submission_id: 51cb11b24f53d638756240b42e31b16fb60e2c41
# seed: 3418055857

# Time:  O(n)
# Space: O(1)

class Solution5(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1