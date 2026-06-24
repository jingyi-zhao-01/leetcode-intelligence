# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-alloys
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-alloys.py
# solution_class: Solution2
# submission_id: 8c0ab7f2d1b9c913cb316900d6d1730b2eea7fa2
# seed: 828740929

# Time:  O(k * nlogn)
# Space: O(n)

# sort, math

class Solution2(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def check(x):
            for machine in composition:
                curr = 0
                for i in xrange(n):
                    curr += max(x*machine[i]-stock[i], 0)*cost[i]
                    if curr > budget:
                        break
                if curr <= budget:
                    return True
            return False

        left, right = 1, min(stock)+budget
        while left <= right:
            mid = left+(right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right