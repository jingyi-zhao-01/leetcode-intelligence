# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-greatest-common-divisors-in-linked-list
# source_path: LeetCode-Solutions-master/Python/insert-greatest-common-divisors-in-linked-list.py
# solution_class: Solution
# submission_id: 13320da4deede320728d69eb0e6213460185b413
# seed: 1355919002

# Time:  O(n)
# Space: O(1)

# linked list

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        curr = head
        while curr.next:
            curr.next = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr = curr.next.next
        return head