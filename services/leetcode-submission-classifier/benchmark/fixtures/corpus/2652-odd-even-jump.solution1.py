# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: odd-even-jump
# source_path: LeetCode-Solutions-master/Python/odd-even-jump.py
# solution_class: Solution
# submission_id: 6fb6d2bfee899b4f048bd46c3dd30a1eef670580
# seed: 2035808844

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def findNext(idx):
            result = [None]*len(idx)
            stack = []
            for i in idx:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        idx = sorted(range(len(A)), key = lambda i: A[i])
        next_higher = findNext(idx)
        idx.sort(key = lambda i: -A[i])
        next_lower = findNext(idx)

        odd, even = [False]*len(A), [False]*len(A)
        odd[-1], even[-1] = True, True
        for i in reversed(xrange(len(A)-1)):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]
        return sum(odd)