# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-k-sorted-lists
# source_path: LeetCode-Solutions-master/Python/merge-k-sorted-lists.py
# solution_class: Solution2
# submission_id: 30a059249b659ef042b3e5ea6558f497133318d6
# seed: 1704139554

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

class Solution2(object):
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)