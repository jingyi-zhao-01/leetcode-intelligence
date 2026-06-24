# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-k-mirror-numbers
# source_path: LeetCode-Solutions-master/Python/sum-of-k-mirror-numbers.py
# solution_class: Solution
# submission_id: 3999a63603a0de8061c1ac413b97c3edcc3625f0
# seed: 889332084

# Time:  O(10^6), the most times of finding x is 665502 (k = 7, n = 30)
# Space: O(1)

class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def mirror(n, base, odd):
            result = n
            if odd:
                n //= base
            while n:
                result = result*base+n%base
                n //= base
            return result

        def num_gen(base):
            prefix_num, total = [1]*2, [base]*2
            odd = 1
            while True:
                x = mirror(prefix_num[odd], base, odd)
                prefix_num[odd] += 1
                if prefix_num[odd] == total[odd]:
                    total[odd] *= base
                    odd ^= 1
                yield x

        def reverse(n, base):
            result = 0
            while n:
                result = result*base+n%base
                n = n//base
            return result

        def mirror_num(gen, base):
            while True:
                x = next(gen)
                if x == reverse(x, base):
                    break
            return x

        base1, base2 = k, 10  # (10, k) is slower
        gen = num_gen(base1)
        return sum(mirror_num(gen, base2) for _ in xrange(n))