# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-days-to-disconnect-island
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-days-to-disconnect-island.py
# solution_class: Solution3
# submission_id: 597cde187c9cf61c241fbeb8461430814a147adc
# seed: 2948547241

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

class Solution3(object):
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

        R, C = len(grid), len(grid[0])
        if count_islands(grid) != 1:
            return 0
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                island_cnt = count_islands(grid)
                grid[i][j] = 1
                if island_cnt != 1:
                    return 1
        return 2