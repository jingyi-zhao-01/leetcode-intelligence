# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-duplicate-number
# source_path: LeetCode-Solutions-master/Python/find-the-duplicate-number.py
# solution_class: Solution
# submission_id: 6b02a098aa1b88cfc2f22b4c1cfea66a38cb7a5c
# seed: 1448428568

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow