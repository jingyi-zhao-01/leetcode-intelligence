# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-to-base-2
# source_path: LeetCode-Solutions-master/Python/convert-to-base-2.py
# solution_class: Solution2
# submission_id: aa34b022c9be4a9a060910c3829f70d56725a026
# seed: 4118142987

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        BASE = -2
        result = []
        while N:
            N, r = divmod(N, BASE)
            if r < 0:
                r -= BASE
                N += 1
            result.append(str(r))
        result.reverse()
        return "".join(result) if result else "0"