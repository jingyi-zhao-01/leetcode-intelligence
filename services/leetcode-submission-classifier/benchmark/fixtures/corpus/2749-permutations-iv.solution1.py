# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations-iv
# source_path: LeetCode-Solutions-master/Python/permutations-iv.py
# solution_class: Solution
# submission_id: c2defeb8eac4079f291556215d69843bf66fa08a
# seed: 1474557285

# Time:  O(n^2)
# Space: O(n)

# combinatorics

class Solution(object):
    def permute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        cnt = [1]*n
        for i in xrange(len(cnt)-1):
            cnt[i+1] = min(cnt[i]*((i+2)//2), k)
        lookup = [False]*n
        for i in xrange(n):
            for j in xrange(n):
                if not (not lookup[j] and ((i == 0 and n%2 == 0) or (j+1)%2 == (1 if not result else (result[-1]%2)^1))):
                    continue
                if k <= cnt[n-1-i]:
                    break
                k -= cnt[n-1-i]
            else:
                return []
            lookup[j] = True
            result.append(j+1)
        return result