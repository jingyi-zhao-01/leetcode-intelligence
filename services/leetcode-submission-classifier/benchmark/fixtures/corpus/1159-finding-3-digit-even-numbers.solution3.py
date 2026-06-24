# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-3-digit-even-numbers
# source_path: LeetCode-Solutions-master/Python/finding-3-digit-even-numbers.py
# solution_class: Solution3
# submission_id: 89ee2eae705dd2c0b0565fc21e25ed881a3dac5a
# seed: 2673445967

# Time:  O(1) ~ O(n), n is 10^3
# Space: O(1)

class Solution3(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 3
        def backtracking(curr, dummy, result):
            if len(curr) == k:
                result.append(reduce(lambda x, y: x*10+y, curr))
                return
            node = dummy.right
            while node:
                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):
                    node = node.right
                    continue
                node.val[1] -= 1
                if node.val[1] == 0:
                    if node.left:
                        node.left.right = node.right
                    if node.right:
                        node.right.left = node.left
                curr.append(node.val[0])
                backtracking(curr, dummy, result)
                curr.pop()
                if node.val[1] == 0:
                    if node.left:
                        node.left.right = node
                    if node.right:
                        node.right.left = node
                node.val[1] += 1
                node = node.right

        prev = dummy = Node()
        for digit, cnt in sorted(map(list, collections.Counter(digits).iteritems())):
            prev.right = Node(val=[digit, cnt], left=prev)
            prev = prev.right
        result = []
        backtracking([], dummy, result)
        return result