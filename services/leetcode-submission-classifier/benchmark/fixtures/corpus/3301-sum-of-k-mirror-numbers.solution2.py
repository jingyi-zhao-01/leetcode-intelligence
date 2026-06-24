# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-k-mirror-numbers
# source_path: LeetCode-Solutions-master/Python/sum-of-k-mirror-numbers.py
# solution_class: Solution2
# submission_id: 0de7102e515e49cce8ca2d4a362d9e50aee32677
# seed: 3013246429

# Time:  O(10^6), the most times of finding x is 665502 (k = 7, n = 30)
# Space: O(1)

class Solution2(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def num_gen(k):
            digits = ['0']
            while True:
                for i in xrange(len(digits)//2, len(digits)): 
                    if int(digits[i])+1 < k:
                        digits[i] = digits[-1-i] = str(int(digits[i])+1)
                        break
                    digits[i] = digits[-1-i] = '0'
                else:
                    digits.insert(0, '1')
                    digits[-1] = '1'
                yield "".join(digits)
        
        def mirror_num(gen):
            while True:
                x = int(next(gen, k), k)
                if str(x) == str(x)[::-1]:
                    break
            return x

        gen = num_gen(k)
        return sum(mirror_num(gen) for _ in xrange(n))