# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mini-parser
# source_path: LeetCode-Solutions-master/Python/mini-parser.py
# solution_class: Solution
# submission_id: 63f68e48cb21613ad18ff791ec86bc29d604ee9a
# seed: 3307581530

# Time:  O(n)
# Space: O(h)

class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def deserialize(self, s):
        if not s:
            return NestedInteger()

        if s[0] != '[':
            return NestedInteger(int(s))

        stk = []

        i = 0
        for j in xrange(len(s)):
            if s[j] == '[':
                stk += NestedInteger(),
                i = j+1
            elif s[j] in ',]':
                if s[j-1].isdigit():
                    stk[-1].add(NestedInteger(int(s[i:j])))
                if s[j] == ']' and len(stk) > 1:
                    cur = stk[-1]
                    stk.pop()
                    stk[-1].add(cur)
                i = j+1

        return stk[-1]