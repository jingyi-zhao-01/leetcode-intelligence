# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-of-one-repeating-character
# source_path: LeetCode-Solutions-master/Python/longest-substring-of-one-repeating-character.py
# solution_class: Solution
# submission_id: e99c77600434dd520a85d4fc7571acfedce96de9
# seed: 24954773

# Time:  O(nlogn)
# Space: O(n)

import itertools


# Template:
# https://github.com/kamyu104/FacebookHackerCup-2021/blob/main/Round%203/auth_ore_ization.py
class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda _: float("inf"),
                 query_fn=lambda x, y: x if y is None else min(x, y),
                 update_fn=lambda x: x):
        self.tree = [None]*(2*2**((N-1).bit_length()))
        self.base = len(self.tree)//2
        self.query_fn = query_fn
        self.update_fn = update_fn
        for i in xrange(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(xrange(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, h):
        x = self.base+i
        self.tree[x] = self.update_fn(h)
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])


# segment tree

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        LEFT, RIGHT, LEFT_LEN, RIGHT_LEN, LEN, MAX_LEN, SIZE = xrange(7)
        def build(i):
            return update(s[i])

        def update(y):
            result = [0]*SIZE
            result[LEFT] = result[RIGHT] = y
            result[LEN] = result[LEFT_LEN] = result[RIGHT_LEN] = result[MAX_LEN] = 1
            return result

        def query(x, y):
            return x if y is None else \
                   [x[LEFT],
                    y[RIGHT],
                    x[LEFT_LEN]+(y[LEFT_LEN] if x[LEFT_LEN] == x[LEN] and x[RIGHT] == y[LEFT] else 0),
                    y[RIGHT_LEN]+(x[RIGHT_LEN] if y[RIGHT_LEN] == y[LEN] and y[LEFT] == x[RIGHT] else 0),
                    x[LEN]+y[LEN],
                    max(x[MAX_LEN], y[MAX_LEN], x[RIGHT_LEN]+y[LEFT_LEN] if x[RIGHT] == y[LEFT] else 0)]
        
        result = []
        st = SegmentTree(len(s), build_fn=build, query_fn=query, update_fn=update)
        for c, i in itertools.izip(queryCharacters, queryIndices):
            st.update(i, c)
            result.append(st.tree[1][MAX_LEN])
        return result