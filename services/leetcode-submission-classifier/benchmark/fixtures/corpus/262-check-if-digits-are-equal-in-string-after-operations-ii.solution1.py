# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-digits-are-equal-in-string-after-operations-ii
# source_path: LeetCode-Solutions-master/Python/check-if-digits-are-equal-in-string-after-operations-ii.py
# solution_class: Solution
# submission_id: c0d8b0212d17b9548d552a034276e0258e51b489
# seed: 1970546472

# Time:  O(nlogn)
# Space: O(1)

# fast exponentiation

class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(mod):
            def decompose(x, mod):  # x = a * mod^cnt
                cnt = 0
                while x > 1 and x%mod == 0:
                    x //= mod
                    cnt += 1
                return x, cnt

            result = cnt = 0
            curr = 1
            for i in xrange(len(s)-1):
                if cnt == 0:
                    result = (result+curr*(ord(s[i])-ord(s[i+1])))%mod
                x, c = decompose(len(s)-2-i, mod)
                curr = (curr*x)%mod
                cnt += c
                x, c = decompose(i+1, mod)
                curr = (curr*pow(x, mod-2, mod))%mod
                cnt -= c
            return result == 0

        return check(2) and check(5)