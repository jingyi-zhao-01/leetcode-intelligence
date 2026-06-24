# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-array-given-subset-sums
# source_path: LeetCode-Solutions-master/Python/find-array-given-subset-sums.py
# solution_class: Solution3
# submission_id: 7e257b52774a828f2b5f893b3cfe28b347e1bab6
# seed: 285988275

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

class Solution3(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        dp = {k: v for k, v in collections.Counter(sums).iteritems()}
        total = reduce(operator.ior, dp.itervalues(), 0)
        basis = total&-total  # find rightmost bit 1
        if basis > 1:
            for k in dp.iterkeys():
                dp[k] //= basis
        sorted_sums = sorted(dp.iterkeys())  # Time: O(2^n * log(2^n)) = O(n * 2^n)
        shift = 0
        result = [0]*(basis.bit_length()-1)
        for _ in xrange(n-len(result)):  # log(2^n) times, each time costs O(2^(n-len(result))), Total Time: O(2^n)
            new_dp = {}
            new_sorted_sums = []
            new_shift = sorted_sums[0]-sorted_sums[1]
            assert(new_shift < 0)
            for x in sorted_sums:
                if not dp[x]:
                    continue
                dp[x-new_shift] -= dp[x]
                new_dp[x-new_shift] = dp[x]
                new_sorted_sums.append(x-new_shift)
            dp = new_dp
            sorted_sums = new_sorted_sums
            if shift in dp:  # contain 0, choose this side
                result.append(new_shift)
            else:  # contain no 0, choose another side and shift 0 offset
                result.append(-new_shift)
                shift -= new_shift
        return result