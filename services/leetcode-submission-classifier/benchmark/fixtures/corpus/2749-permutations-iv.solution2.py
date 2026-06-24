# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations-iv
# source_path: LeetCode-Solutions-master/Python/permutations-iv.py
# solution_class: Solution2
# submission_id: e0c7294d3782dc6bbd8210350b18d63429647f62
# seed: 633968463

# Time:  O(n^2)
# Space: O(n)

# combinatorics

class Solution2(object):
    def permute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        fact = [1]*(((n-1)+1)//2+1)
        for i in xrange(len(fact)-1):
            fact[i+1] = fact[i]*(i+1)
        lookup = [False]*n
        for i in xrange(n):
            cnt = fact[(n-1-i)//2]*fact[((n-1-i)+1)//2]
            for j in xrange(n):
                if not (not lookup[j] and ((i == 0 and n%2 == 0) or (j+1)%2 == (1 if not result else (result[-1]%2)^1))):
                    continue
                if k <= cnt:
                    break
                k -= cnt
            else:
                return []
            lookup[j] = True
            result.append(j+1)
        return result