# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: copy-list-with-random-pointer
# source_path: LeetCode-Solutions-master/Python/copy-list-with-random-pointer.py
# solution_class: Solution2
# submission_id: 14e0a9677e00d57836a91ad568a4b7cb7d1117fe
# seed: 3217351854

# Time:  O(n)
# Space: O(1)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution2(object):
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dummy = Node(0)
        current, prev, copies = head, dummy, {}

        while current:
            copied = Node(current.val)
            copies[current] = copied
            prev.next = copied
            prev, current = prev.next, current.next

        current = head
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            current = current.next

        return dummy.next