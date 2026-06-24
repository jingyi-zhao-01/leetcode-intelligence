# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-books-you-can-take
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-books-you-can-take.py
# solution_class: Solution
# submission_id: 9b5221f42c6aae4619c9d5a43ea67585c9d3de7a
# seed: 4011746483

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def maximumBooks(self, books):
        """
        :type books: List[int]
        :rtype: int
        """
        def count(right, l):
            left = max(right-l+1, 0)
            return (left+right)*(right-left+1)//2
        
        result = curr = 0
        stk = [-1]
        for i in xrange(len(books)):
            while stk[-1] != -1 and books[stk[-1]] >= books[i]-(i-stk[-1]):
                j = stk.pop()
                curr -= count(books[j], j-stk[-1])
            curr += count(books[i], i-stk[-1])
            stk.append(i)
            result = max(result, curr)
        return result