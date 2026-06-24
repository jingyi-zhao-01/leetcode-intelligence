# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-an-original-string-exists-given-two-encoded-strings
# source_path: LeetCode-Solutions-master/Python/check-if-an-original-string-exists-given-two-encoded-strings.py
# solution_class: Solution2
# submission_id: defe675cd27d6ff06c437c988980cf804c8223d1
# seed: 991113061

# Time:  O(m * n * k), k is the max number of consecutive digits in s1 and s2
# Space: O(m * n * k)

# top-down dp (faster since accessing less states)

class Solution2(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def memoization(s1, s2, i, j, k, lookup):
            if (i, j, k) not in lookup:
                if i == len(s1) and j == len(s2):
                    lookup[(i, j, k)] = (k == 0)
                elif i != len(s1) and s1[i].isdigit():
                    lookup[(i, j, k)] = False
                    for ni in xrange(i+1, len(s1)+1):
                        if (ni == len(s1) or s1[ni] != '0') and memoization(s1, s2, ni, j, k+int(s1[i:ni]), lookup):
                            lookup[(i, j, k)] = True
                            break
                        if ni == len(s1) or not s1[ni].isdigit():
                            break
                elif j != len(s2) and s2[j].isdigit():
                    lookup[(i, j, k)] = False
                    for nj in xrange(j+1, len(s2)+1):
                        if (nj == len(s2) or s2[nj] != '0') and memoization(s1, s2, i, nj, k-int(s2[j:nj]), lookup):
                            lookup[(i, j, k)] = True
                            break
                        if nj == len(s2) or not s2[nj].isdigit():
                            break
                elif k < 0:
                    lookup[(i, j, k)] = memoization(s1, s2, i+1, j, k+1, lookup) if i != len(s1) else False
                elif k > 0:
                    lookup[(i, j, k)] = memoization(s1, s2, i, j+1, k-1, lookup) if j != len(s2) else False
                else:
                    lookup[(i, j, k)] = memoization(s1, s2, i+1, j+1, k, lookup) if i != len(s1) and j != len(s2) and s1[i] == s2[j] else False
            return lookup[(i, j, k)]

        return memoization(s1, s2, 0, 0, 0, {})