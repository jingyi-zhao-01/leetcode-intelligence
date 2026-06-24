# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-total-strength-of-wizards
# source_path: LeetCode-Solutions-master/Python/sum-of-total-strength-of-wizards.py
# solution_class: Solution
# submission_id: 9fc8ead577214489580d04e89285747e45357f0d
# seed: 201203715

# Time:  O(n)
# Space: O(n)

# mono stack, prefix sum, optimized from solution2

class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        curr = 0
        prefix = [0]*(len(strength)+1)
        for i in xrange(len(strength)):
            curr = (curr+strength[i])%MOD
            prefix[i+1] = (prefix[i]+curr)%MOD
        stk, result = [-1], 0
        for i in xrange(len(strength)+1):
            while stk[-1] != -1 and (i == len(strength) or strength[stk[-1]] >= strength[i]):
                x, y, z = stk[-2]+1, stk.pop(), i-1
                # assert(all(strength[j] >= strength[y] for j in xrange(x, y+1)))
                # assert(all(strength[j] > strength[y] for j in xrange(y+1, z+1)))
                result = (result+(strength[y]*((y-x+1)*(prefix[z+1]-prefix[y])-(z-y+1)*(prefix[y]-prefix[max(x-1, 0)]))))%MOD
            stk.append(i)
        return result