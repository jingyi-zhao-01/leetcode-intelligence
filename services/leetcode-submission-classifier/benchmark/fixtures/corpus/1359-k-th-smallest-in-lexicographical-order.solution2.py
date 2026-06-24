# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-th-smallest-in-lexicographical-order
# source_path: LeetCode-Solutions-master/Python/k-th-smallest-in-lexicographical-order.py
# solution_class: Solution2
# submission_id: 57f72e768bcba3853a6305f7729e89516b508a12
# seed: 1077148330

# Time:  O(logn)
# Space: O(logn)

class Solution2(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(n, prefix):
            result, number = 0, 1
            while prefix <= n:
                result += number
                prefix *= 10
                number *= 10
            result -= max(number/10 - (n - prefix/10 + 1), 0)
            return result

        def findKthNumberHelper(n, k, cur, index):
            if cur:
                index += 1
                if index == k:
                    return (cur, index)

            i = int(cur == 0)
            while i <= 9:
                cur = cur * 10 + i
                cnt = count(n, cur)
                if k > cnt + index:
                    index += cnt
                elif cur <= n:
                    result = findKthNumberHelper(n, k, cur, index)
                    if result[0]:
                        return result
                i += 1
                cur /= 10
            return (0, index)

        return findKthNumberHelper(n, k, 0, 0)[0]