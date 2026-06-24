# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-3-digit-even-numbers
# source_path: LeetCode-Solutions-master/Python/finding-3-digit-even-numbers.py
# solution_class: Solution
# submission_id: 8b4999d228aac794ec9c30ac201f3df1b0c1853b
# seed: 682227946

# Time:  O(1) ~ O(n), n is 10^3
# Space: O(1)

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 3
        def backtracking(curr, cnt, result):
            if len(curr) == k:
                result.append(reduce(lambda x, y: x*10+y, curr))
                return
            for i, c in enumerate(cnt):
                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):
                    continue
                cnt[i] -= 1
                curr.append(i)
                backtracking(curr, cnt, result)
                curr.pop()
                cnt[i] += 1

        cnt = [0]*10
        for d in digits:
            cnt[d] += 1
        result = []
        backtracking([], cnt, result)
        return result