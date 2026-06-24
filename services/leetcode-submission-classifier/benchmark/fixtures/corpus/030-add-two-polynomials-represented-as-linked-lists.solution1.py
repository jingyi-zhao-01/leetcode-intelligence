# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-two-polynomials-represented-as-linked-lists
# source_path: LeetCode-Solutions-master/Python/add-two-polynomials-represented-as-linked-lists.py
# solution_class: Solution
# submission_id: 289bb034654f7d27c180e3a35ec5735f74b72a74
# seed: 3940614170

# Time:  O(m + n)
# Space: O(1)

class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        pass

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        curr = dummy = PolyNode()
        while poly1 and poly2:
            if poly1.power > poly2.power:
                curr.next = poly1
                curr = curr.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                curr.next = poly2
                curr = curr.next
                poly2 = poly2.next
            else:
                coef = poly1.coefficient+poly2.coefficient
                if coef:
                    curr.next = PolyNode(coef, poly1.power)
                    curr = curr.next
                poly1, poly2 = poly1.next, poly2.next
        curr.next = poly1 or poly2
        return dummy.next