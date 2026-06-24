# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: copy-list-with-random-pointer
# source_path: LeetCode-Solutions-master/Python/copy-list-with-random-pointer.py
# solution_class: Solution
# submission_id: 0212957c41aa1c77dfe3c142b91266f9d7361a42
# seed: 2947125327

# Time:  O(n)
# Space: O(1)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution(object):
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # copy and combine copied list with original list
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next

        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # split copied list from combined one
        dummy = Node(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next