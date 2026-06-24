# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-doubly-linked-list-to-array-i
# source_path: LeetCode-Solutions-master/Python/convert-doubly-linked-list-to-array-i.py
# solution_class: Solution
# submission_id: adf80d7fbfb080f89f8de50bdef54171f75c9ade
# seed: 63711589

# Time:  O(n)
# Space: O(1)

# linked list

class Solution:
    def toArray(self, head):
        """
        :type head: Node
        :rtype: List[int]
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result