# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-doubly-linked-list-to-array-ii
# source_path: LeetCode-Solutions-master/Python/convert-doubly-linked-list-to-array-ii.py
# solution_class: Solution
# submission_id: 7b66b11eb87a20a00cb2a89e7ee74b6b51112c90
# seed: 1481361974

# Time:  O(n)
# Space: O(1)

# linked list

class Solution:
    def toArray(self, node):
        """
        :type head: Node
        :rtype: List[int]
        """
        while node.prev:
            node = node.prev
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result