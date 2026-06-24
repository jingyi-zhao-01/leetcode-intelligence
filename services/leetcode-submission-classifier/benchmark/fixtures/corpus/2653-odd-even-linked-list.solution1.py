# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: odd-even-linked-list
# source_path: LeetCode-Solutions-master/Python/odd-even-linked-list.py
# solution_class: Solution
# submission_id: cd3205c8db22e77af618230dccf7b1b93775e843
# seed: 3727546409

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd_tail, cur = head, head.next
            while cur and cur.next:
                even_head = odd_tail.next
                odd_tail.next = cur.next
                odd_tail = odd_tail.next
                cur.next = odd_tail.next
                odd_tail.next = even_head
                cur = cur.next
        return head