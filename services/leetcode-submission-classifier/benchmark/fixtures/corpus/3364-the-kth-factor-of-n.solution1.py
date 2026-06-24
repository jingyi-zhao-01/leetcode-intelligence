# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-kth-factor-of-n
# source_path: LeetCode-Solutions-master/Python/the-kth-factor-of-n.py
# solution_class: Solution
# submission_id: 455e4123c7da38eb63c1b55ddd1ba7c8dc81ee8c
# seed: 125307467

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def kth_factor(n, k=0):
            mid = None
            i = 1
            while i*i <= n:
                if not n%i:
                    mid = i
                    k -= 1
                    if not k:
                        break
                i += 1
            return mid, -k
    
        mid, count = kth_factor(n)
        total = 2*count-(mid*mid == n)
        if k > total:
            return -1
        result = kth_factor(n, k if k <= count else total-(k-1))[0]
        return result if k <= count else n//result