# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-three
# source_path: LeetCode-Solutions-master/Python/power-of-three.py
# solution_class: Solution2
# submission_id: 38dfd25a955937f2b6cfadc22cdbd96d39b30c7b
# seed: 2245189505

# Time:  O(1)
# Space: O(1)

import math

class Solution2(object):
    def isPowerOfThree(self, n):
        return n > 0 and (math.log10(n)/math.log10(3)).is_integer()