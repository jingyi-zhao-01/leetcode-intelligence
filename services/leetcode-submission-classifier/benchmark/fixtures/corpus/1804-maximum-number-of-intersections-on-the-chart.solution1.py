# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-intersections-on-the-chart
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-intersections-on-the-chart.py
# solution_class: Solution
# submission_id: 84c02ab62b1dc3a02b564e78e6523ad516389ca8
# seed: 1039520643

# Time:  O(nlogn)
# Space: O(n)

# sort, line sweep, coordinate compression

class Solution(object):
    def maxIntersectionCount(self, y):
        """
        :type y: List[int]
        :rtype: int
        """
        val_to_idx = {x:i for i, x in enumerate(sorted(set(y)))}
        cnts = [0]*(2*len(val_to_idx)+1)
        for i in xrange(len(y)-1):
            # [y[i], y[i+1]) <=> [y[i], y[i+1]-0.5] <=> [2*y[i], 2*y[i+1]-1]
            left, right = 2*val_to_idx[y[i]], 2*val_to_idx[y[i+1]]+(-1 if y[i] < y[i+1] else +1)
            cnts[min(left, right)] += 1
            cnts[max(left, right)+1] -= 1
        # [y[i], y[i]] <=> [2*y[i], 2*y[i]]
        cnts[2*val_to_idx[y[-1]]] += 1
        cnts[2*val_to_idx[y[-1]]+1] -= 1
        result = cnt = 0
        for c in cnts:
            cnt += c
            result = max(result, cnt)
        return result