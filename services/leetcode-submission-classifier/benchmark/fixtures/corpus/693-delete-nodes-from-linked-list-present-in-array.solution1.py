# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-nodes-from-linked-list-present-in-array
# source_path: LeetCode-Solutions-master/Python/delete-nodes-from-linked-list-present-in-array.py
# solution_class: Solution
# submission_id: ec4abd531c3ea9fa56269b22501f2cf3b2189955
# seed: 3263273622

# Time:  O(n)
# Space: O(m)

# hash table, linked list

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lookup = set(nums)
        curr = dummy = ListNode(0, head)
        while curr.next:
            if curr.next.val not in lookup:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return dummy.next