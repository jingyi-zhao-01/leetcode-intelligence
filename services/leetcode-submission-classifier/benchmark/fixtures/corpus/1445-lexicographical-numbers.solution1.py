# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographical-numbers
# source_path: LeetCode-Solutions-master/Python/lexicographical-numbers.py
# solution_class: Solution
# submission_id: 6b3e74b6ebd122043398821538b1545471ada1c4
# seed: 1823182965

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lexicalOrder(self, n):
        result = []

        i = 1
        while len(result) < n:
            k = 0
            while i * 10**k <= n:
                result.append(i * 10**k)
                k += 1

            num = result[-1] + 1
            while num <= n and num % 10:
                result.append(num)
                num += 1

            if not num % 10:
                num -= 1
            else:
                num /= 10

            while num % 10 == 9:
                num /= 10

            i = num+1

        return result