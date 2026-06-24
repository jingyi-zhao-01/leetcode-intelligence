# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: form-largest-integer-with-digits-that-add-up-to-target
# source_path: LeetCode-Solutions-master/Python/form-largest-integer-with-digits-that-add-up-to-target.py
# solution_class: Solution2
# submission_id: f2ccc35fb3666e2455f83ff154ff948e074e5ff1
# seed: 3158294353

# Time:  O(t)
# Space: O(t)

class Solution2(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        def key(bag):
            return sum(bag), bag
        
        dp = [[0]*9]
        for t in xrange(1, target+1):
            dp.append([])
            for d, c in enumerate(cost):
                if t < c or not dp[t-c]:
                    continue
                curr = dp[t-c][:]
                curr[~d] += 1
                if key(curr) > key(dp[t]):
                    dp[-1] = curr        
        if not dp[-1]:
            return "0"
        return "".join(str(9-i)*c for i, c in enumerate(dp[-1]))