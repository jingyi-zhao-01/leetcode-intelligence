# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-number-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/sum-of-number-and-its-reverse.py
# solution_class: Solution
# submission_id: 9399745866f353e655c8097762348b0e727c36a4
# seed: 3602331773

# Time:  O(2^(log10(n)/2)) = O(n^(1/(2*log2(10))))
# Space: O(log10(n)/2)

# backtracking

class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def backtracking(num, chosen):
            if num == 0:
                return True
            if chosen == 1:
                return False
            if num <= 18:
                return (num%2 == 0) or (num == 11 and chosen == 0)
            if chosen == 2:
                return False
            for x in (num%10, 10+num%10):
                if not (1 <= x <= 18):
                    continue
                base = 11
                if chosen:
                    base = chosen
                else:
                    while x*((base-1)*10+1) <= num:
                        base = (base-1)*10+1
                if num-x*base >= 0 and backtracking((num-x*base)//10, base//100+1):
                    return True
            return False

        return backtracking(num, 0)