# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-array-given-subset-sums
# source_path: LeetCode-Solutions-master/Python/find-array-given-subset-sums.py
# solution_class: Solution5
# submission_id: 0245bd780196d304ca74f47e8a24ebf26040ddb7
# seed: 4269860872

# Time:  O(n * 2^n), len(sums) = 2^n
# Space: O(1)

# [proof]
# - let d = sorted_sums[0]-sorted_sums[1] and d != -d (d = 0 is trival), where one of +d/-d is the smallest positive or largest negative number of the original solution of [S1, ..., S(2^n)]
# - given Sp-d = 0 for some p in [1, 2^n] and Sq-(-d) = 0 for some q in [1, 2^n]
#   assume d is a number of the original solution of [S1, ..., S(2^n)] (the proof where -d is a number of the original solution is vice versa)
#   let Sq = x1+...+xi where 1 <= i <= n-1
#   let [d]+[x1, ..., xi]+[x(i+1), ..., x(n-1)] be the original solution
#   => new_sums([S1, ..., S(2^n)], d)
#      = subset_sums([x1, ..., xi]+[x(i+1), ..., x(n-1)])
#   if we choose -d as a number of a solution of [S1, ..., S(2^n)]
#   => new_sums([S1, ..., S(2^n)], -d)
#      = new_sums([S1, ..., S(2^n)], -(x1+...+xi))
#      = subset_sums([(-x1), ..., (-xi)]+[x(i+1), ..., x(n-1)])
#      => [-d]+[(-x1), ..., (-xi)]+[x(i+1), ..., x(n-1)] is also a solution
#
# [conclusion]
# - if new_sums with +d/-d (including d = 0) both contain zero, we can choose either one
# - if only one of new_sums with +d/-d contains zero, we can only choose the one with zero since subset_sums must contain zero

# optimized from solution4 (not using dict), runtime: 1040 ms

class Solution5(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        dp = OrderedDict(sorted(collections.Counter(sums).iteritems()))  # Time: O(2^n * log(2^n)) = O(n * 2^n)
        shift = 0
        result = []
        for _ in xrange(n):  # log(2^n) times, each time costs O(2^(n-len(result))), Total Time: O(2^n)
            new_dp = OrderedDict()
            it = iter(dp)
            min_sum = next(it)
            new_shift = min_sum-next(it) if dp[min_sum] == 1 else 0
            assert(new_shift <= 0)
            for x in dp.iterkeys():
                if not dp[x]:
                    continue
                dp[x-new_shift] -= dp[x] if new_shift else dp[x]//2
                new_dp[x-new_shift] = dp[x]
            dp = new_dp
            if shift in dp:  # contain 0, choose this side
                result.append(new_shift)
            else:  # contain no 0, choose another side and shift 0 offset
                result.append(-new_shift)
                shift -= new_shift
        return result