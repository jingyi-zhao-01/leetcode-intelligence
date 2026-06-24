# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-linked-list
# source_path: LeetCode-Solutions-master/Python/palindrome-linked-list.py
# solution_class: Solution
# submission_id: 5dd5f8edb9f19ce72ea1d1fb37bfdab39ec33a6c
# seed: 4289923891

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palindrome