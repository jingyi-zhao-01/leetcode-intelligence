# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: four-divisors
# source_path: LeetCode-Solutions-master/Python/four-divisors.py
# solution_class: Solution2
# submission_id: 57b7fc9aeed0f1524334036d0d864ac9f745858a
# seed: 2432304613

# Time:  O(n * sqrt(n))
# Space: O(1)

class Solution2(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def factorize(x):
            result = []
            d = 2
            while d*d <= x:
                e = 0
                while x%d == 0:
                    x //= d
                    e += 1
                if e:
                    result.append([d, e])
                d += 1 if d == 2 else 2
            if x > 1:
                result.append([x, 1])
            return result
       
        result = 0
        for facs in itertools.imap(factorize, nums):
            if len(facs) == 1 and facs[0][1] == 3:
                p = facs[0][0]
                result += (p**4-1)//(p-1)  # p^0 + p^1 +p^2 +p^3
            elif len(facs) == 2 and facs[0][1] == facs[1][1] == 1:
                p, q = facs[0][0], facs[1][0]
                result += (1 + p) * (1 + q)
        return result