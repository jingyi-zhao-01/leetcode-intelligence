# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-k-sorted-lists
# source_path: LeetCode-Solutions-master/Python/merge-k-sorted-lists.py
# solution_class: Solution3
# submission_id: 1684de678c48051d1e0ad66edc523ea5e9686401
# seed: 4003169841

# Time:  O(nlogk)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)


# Merge two by two solution.

class Solution3(object):
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next