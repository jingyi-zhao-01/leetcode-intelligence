# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: winner-of-the-linked-list-game
# source_path: LeetCode-Solutions-master/Python/winner-of-the-linked-list-game.py
# solution_class: Solution
# submission_id: 184dc848092481d9ee1e1f2a9b1954610ffd2bdc
# seed: 1191637712

# Time:  O(n)
# Space: O(1)

# linked list

class Solution(object):
    def gameResult(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: str
        """
        cnt = 0
        while head:
            cnt += cmp(head.val, head.next.val)
            head = head.next.next
        return "Tie" if cnt == 0 else "Odd" if cnt < 0 else "Even"