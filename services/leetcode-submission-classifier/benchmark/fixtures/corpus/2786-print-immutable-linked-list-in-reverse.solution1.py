# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-immutable-linked-list-in-reverse
# source_path: LeetCode-Solutions-master/Python/print-immutable-linked-list-in-reverse.py
# solution_class: Solution
# submission_id: ada134238d9bd46ac722a51cc4f7655586dc9c0e
# seed: 2245609888

# Time:  O(n)
# Space: O(sqrt(n))

import math

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        def print_nodes(head, count):
            nodes = []
            while head and len(nodes) != count:
                nodes.append(head)
                head = head.getNext()
            for node in reversed(nodes):
                node.printValue()
                   
        count = 0
        curr = head
        while curr:
            curr = curr.getNext()
            count += 1
        bucket_count = int(math.ceil(count**0.5))
        
        buckets = []
        count = 0
        curr = head
        while curr:
            if count % bucket_count == 0:
                buckets.append(curr)
            curr = curr.getNext()
            count += 1
        for node in reversed(buckets):
            print_nodes(node, bucket_count)