# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-x-and-y-equal
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-x-and-y-equal.py
# solution_class: Solution2
# submission_id: 71aaf88c70f4d40621b404ba87414c1c4b2aafbc
# seed: 917541097

# Time:  O(x)
# Space: O(x)

# memoization

class Solution2(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        if y >= x:
            return y-x
        upper_bound = x+(x-y)
        result = 0
        lookup = {x}
        q = [x]
        while q:
            new_q = []
            for x in q:
                if x == y:
                    return result
                candidates = [x+1, x-1]
                for d in (5, 11):
                    if x%d == 0:
                        candidates.append(x//d)
                for new_x in candidates:
                    if not (0 <= new_x <= upper_bound and new_x not in lookup):
                        continue
                    lookup.add(new_x)
                    new_q.append(new_x)
            q = new_q
            result += 1
        return -1