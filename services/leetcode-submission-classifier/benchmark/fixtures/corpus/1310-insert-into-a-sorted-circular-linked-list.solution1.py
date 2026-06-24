# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-into-a-sorted-circular-linked-list
# source_path: LeetCode-Solutions-master/Python/insert-into-a-sorted-circular-linked-list.py
# solution_class: Solution
# submission_id: f196ba6f8f6b95b5498adb95fa9534edee57a60d
# seed: 3231216008

# Time:  O(n)
# Space: O(1)

class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        def insertAfter(node, val):
            node.next = Node(val, node.next)
        
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node

        curr = head
        while True:
            if curr.val < curr.next.val:
                if curr.val <= insertVal and \
                   insertVal <= curr.next.val:
                    insertAfter(curr, insertVal)
                    break
            elif curr.val > curr.next.val:
                if curr.val <= insertVal or \
                   insertVal <= curr.next.val:
                    insertAfter(curr, insertVal)
                    break
            else:
                if curr.next == head:
                    insertAfter(curr, insertVal)
                    break
            curr = curr.next
        return head