# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-number
# source_path: LeetCode-Solutions-master/Python/valid-number.py
# solution_class: Solution2
# submission_id: 0f876d99ba2c4eaa69b401495c9909a1d0b514dd
# seed: 2250895013

# Time:  O(n)
# Space: O(1)

class InputType(object):
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5


# regular expression: "^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png

class Solution2(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))