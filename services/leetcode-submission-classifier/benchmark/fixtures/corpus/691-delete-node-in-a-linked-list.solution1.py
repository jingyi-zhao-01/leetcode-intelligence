# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-node-in-a-linked-list
# source_path: LeetCode-Solutions-master/Python/delete-node-in-a-linked-list.py
# solution_class: Solution
# submission_id: bc0cd91667ca160dc236bff1352a40949aaefc19
# seed: 1802242364

# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node and node.next:
            node_to_delete = node.next
            node.val = node_to_delete.val
            node.next = node_to_delete.next
            del node_to_delete