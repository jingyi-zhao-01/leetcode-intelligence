# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-complete-all-deliveries
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-complete-all-deliveries.py
# solution_class: Solution
# submission_id: 91c2b8231b24a18605ea2704c712216b20ce26bb
# seed: 1375324127

# Time:  O(logr + logd)
# Space: O(1)

# binary search, number theory

class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a,b)*b

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
    
        def check(t):
            return t-t//r[0] >= d[0] and t-t//r[1] >= d[1] and t-t//l >= d[0]+d[1]

        l = lcm(r[0], r[1])
        return binary_search(sum(d), sum(d)*2, check)