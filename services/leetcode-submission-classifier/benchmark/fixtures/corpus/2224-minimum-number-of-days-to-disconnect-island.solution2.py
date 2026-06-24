# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-days-to-disconnect-island
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-days-to-disconnect-island.py
# solution_class: Solution2
# submission_id: 7825b1ec8b11be10f8eb61ca841747e2ea6d75e6
# seed: 2911871790

# Time:  O(m * n)
# Space: O(m * n)

# template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20B/railroad_maintenance.py3
# Reference: https://en.wikipedia.org/wiki/Biconnected_component#Algorithms
def iter_get_articulation_points(graph, v):  # modified
    def iter_dfs(v, p):
        stk = [(1, (v, p))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                v, p = args
                index[v] = index_counter[0]
                lowlinks[v] = index_counter[0]
                index_counter[0] += 1
                children_count = [0]
                is_cut = [False]
                stk.append((4, (v, p, children_count, is_cut)))
                for w in reversed(graph[v]):
                    if w == p:
                        continue
                    stk.append((2, (w, v, children_count, is_cut)))
            elif step == 2:
                w, v, children_count, is_cut = args
                if index[w] == -1:
                    children_count[0] += 1
                    stk.append((3, (w, v, is_cut)))
                    stk.append((1, (w, v)))
                else:
                    lowlinks[v] = min(lowlinks[v], index[w])
            elif step == 3:
                w, v, is_cut = args
                if lowlinks[w] >= index[v]:
                    is_cut[0] = True
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif step == 4:
                v, p, children_count, is_cut = args
                if (p != -1 and is_cut[0]) or (p == -1 and children_count[0] >= 2):
                    cutpoints.append(v)
    index_counter, index, lowlinks = [0], [-1]*len(graph), [0]*len(graph)
    cutpoints = []
    iter_dfs(v, -1)  # modified
    return cutpoints


# flood fill, tarjan's algorithm, articulation points

class Solution2(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        def floodfill(grid, i, j, lookup):
            stk = [(i, j)]
            lookup[i][j] = 1
            while stk:
                i, j = stk.pop()
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < R and 0 <= nj < C and grid[ni][nj] and not lookup[ni][nj]):
                        continue
                    lookup[ni][nj] = 1
                    stk.append((ni, nj))
         
        def count_islands(grid):
            lookup = [[0]*C for _ in xrange(R)]
            island_cnt = 0
            for i in xrange(R):
                for j in xrange(C):
                    if grid[i][j] == 0 or lookup[i][j]:
                        continue
                    island_cnt += 1
                    floodfill(grid, i, j, lookup)
            return island_cnt
    
        def merge(i):
            r, c = divmod(i, C)
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                ni = nr*C+nc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == grid[r][c] and lookup[ni]:
                    uf.union_set(i, ni)

        def check(i):
            r, c = divmod(i, C)
            if grid[r][c] == 0:
                return False
            lookup = set()
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if  0 <= nr < R and 0 <= nc < C and grid[nr][nc] == grid[r][c]:
                    lookup.add(uf.find_set(nr*C+nc))
            return len(lookup) != 1

        def dfs(left, right):
            if left == right:
                return check(left)
            mid = left + (right-left)//2
            l1, r1, l2, r2 = left, mid, mid+1, right
            for _ in xrange(2):
                uf.snapshot()
                for i in xrange(l1, r1+1):
                    lookup[i] = True
                    merge(i)
                if dfs(l2, r2):
                    return True
                for i in xrange(l1, r1+1):
                    lookup[i] = False
                uf.rollback()
                l1, r1, l2, r2 = l2, r2, l1, r1
            return False

        R, C = len(grid), len(grid[0])
        if count_islands(grid) != 1:
            return 0
        uf = PersistentUnionFind(R*C)
        lookup = [False]*(R*C)
        return 1 if dfs(0, R*C-1) else 2