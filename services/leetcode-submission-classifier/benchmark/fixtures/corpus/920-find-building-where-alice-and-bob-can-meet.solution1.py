# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-building-where-alice-and-bob-can-meet
# source_path: LeetCode-Solutions-master/Python/find-building-where-alice-and-bob-can-meet.py
# solution_class: Solution
# submission_id: 51004ed3c53bd3e4afafe335c290000782da79e5
# seed: 86483731

# Time:  O(n + qlogn)
# Space: O(n)

# online solution, segment tree, binary search

class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Range Maximum Query
        class SegmentTree(object):
            def __init__(self, N,
                         build_fn=lambda _: None,
                         query_fn=lambda x, y: max(x, y)):
                self.tree = [None]*(2*2**((N-1).bit_length()))
                self.build_fn = build_fn
                self.query_fn = query_fn
                self.build(0, N-1, 1)
            
            def build(self, left, right, idx):
                if left == right:
                    self.tree[idx] = self.build_fn(left)
                    return 
                mid = left + (right-left)//2
                self.build(left, mid, idx*2)
                self.build(mid+1, right, idx*2+1)
                self.tree[idx] = self.query_fn(self.tree[idx*2], self.tree[idx*2+1])

            def binary_search(self, L, R, left, right, idx, h):
                if right < L or left > R:
                    return -1
                if L <= left and right <= R:
                    if not self.tree[idx] > h:
                        return -1
                    if left == right:
                        return left
                mid = left + (right-left)//2
                i = self.binary_search(L, R, left, mid, idx*2, h)
                return i if i != -1 else self.binary_search(L, R, mid+1, right, idx*2+1, h)

        def build(i):
            return heights[i]

        result = [-1]*len(queries)
        st = SegmentTree(len(heights), build_fn=build)
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
                continue
            result[i] = st.binary_search(b+1, len(heights)-1, 0, len(heights)-1, 1, heights[a])
        return result