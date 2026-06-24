# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-an-original-string-exists-given-two-encoded-strings
# source_path: LeetCode-Solutions-master/Python/check-if-an-original-string-exists-given-two-encoded-strings.py
# solution_class: Solution
# submission_id: 083bdafc318b0e878ab66c287418da8e62943c2d
# seed: 1290498442

# Time:  O(m * n * k), k is the max number of consecutive digits in s1 and s2
# Space: O(m * n * k)

# top-down dp (faster since accessing less states)

class Solution(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def general_possible_numbers(s):  # Time: O(2^l), Space: O(2^l), l is the length of consecutive digits, and l is at most 3
            dp = [set() for _ in xrange(len(s))]
            for i in xrange(len(s)):
                curr, basis = 0, 1
                for j in reversed(xrange(i+1)):
                    curr += int(s[j])*basis
                    basis *= 10
                    if s[j] == '0':
                        continue
                    if j == 0:
                        dp[i].add(curr)
                    else:
                        dp[i].update(x+curr for x in dp[j-1])        
            return dp[-1]

        def optimized_possible_numbers(s):
            assert(len(s) <= 3)
            result = {int(s)}
            if len(s) >= 2:
                if s[1] != '0':
                    result.add(int(s[:1])+int(s[1:]))
            if len(s) >= 3:
                if s[2] != '0':
                    result.add(int(s[:2])+int(s[2:]))
                    if s[1] != '0':
                        result.add(int(s[0:1])+int(s[1:2])+int(s[2:]))
            return result
    
        def memoization(s1, s2, i, j, k, lookup):
            if (i, j, k) not in lookup:
                if i == len(s1) and j == len(s2):
                    lookup[(i, j, k)] = (k == 0)
                elif i != len(s1) and s1[i].isdigit():
                    lookup[(i, j, k)] = False
                    for ni in xrange(i+1, len(s1)+1):
                        if ni == len(s1) or not s1[ni].isdigit():
                            break
                    for x in optimized_possible_numbers(s1[i:ni]):
                        if memoization(s1, s2, ni, j, k+x, lookup):
                            lookup[(i, j, k)] = True
                            break
                elif j != len(s2) and s2[j].isdigit():
                    lookup[(i, j, k)] = False
                    for nj in xrange(j+1, len(s2)+1):
                        if nj == len(s2) or not s2[nj].isdigit():
                            break
                    for x in optimized_possible_numbers(s2[j:nj]):
                        if memoization(s1, s2, i, nj, k-x, lookup):
                            lookup[(i, j, k)] = True
                            break
                elif k < 0:
                    lookup[(i, j, k)] = memoization(s1, s2, i+1, j, k+1, lookup) if i != len(s1) else False
                elif k > 0:
                    lookup[(i, j, k)] = memoization(s1, s2, i, j+1, k-1, lookup) if j != len(s2) else False
                else:
                    lookup[(i, j, k)] = memoization(s1, s2, i+1, j+1, k, lookup) if i != len(s1) and j != len(s2) and s1[i] == s2[j] else False
            return lookup[(i, j, k)]

        return memoization(s1, s2, 0, 0, 0, {})