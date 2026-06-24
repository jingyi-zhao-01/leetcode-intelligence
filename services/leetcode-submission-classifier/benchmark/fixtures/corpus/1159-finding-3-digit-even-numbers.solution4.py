# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-3-digit-even-numbers
# source_path: LeetCode-Solutions-master/Python/finding-3-digit-even-numbers.py
# solution_class: Solution4
# submission_id: 49cc1d8aa9de969f38278a3947a900b64ca913ab
# seed: 2427604749

# Time:  O(1) ~ O(n), n is 10^3
# Space: O(1)

class Solution4(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 3
        def backtracking(curr, digit_cnt, result):
            if len(curr) == k:
                result.append(reduce(lambda x, y: x*10+y, curr))
                return
            for i, (digit, cnt) in enumerate(digit_cnt):
                if (not curr and digit == 0) or (len(curr) == k-1 and digit%2 != 0):
                    continue
                digit_cnt[i][1] -= 1
                digit_cnt[i], digit_cnt[-1] = digit_cnt[-1], digit_cnt[i]
                removed = []
                if digit_cnt[-1][1] == 0:
                    removed = digit_cnt.pop()
                curr.append(digit)
                backtracking(curr, digit_cnt, result)
                curr.pop()
                if removed:
                    digit_cnt.append(removed)
                digit_cnt[i], digit_cnt[-1] = digit_cnt[-1], digit_cnt[i]
                digit_cnt[i][1] += 1

        cnt = collections.Counter(digits)
        digit_cnt = map(list, cnt.iteritems())
        result = []
        backtracking([], digit_cnt, result)
        result.sort()
        return result