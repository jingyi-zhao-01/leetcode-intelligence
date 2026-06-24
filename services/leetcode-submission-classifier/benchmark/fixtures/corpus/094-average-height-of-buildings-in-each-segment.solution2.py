# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-height-of-buildings-in-each-segment
# source_path: LeetCode-Solutions-master/Python/average-height-of-buildings-in-each-segment.py
# solution_class: Solution2
# submission_id: 4d41edfa389d840ce1dc04ac9060efb2e1e57133
# seed: 3102842954

# Time:  O(nlogn)
# Space: O(n)

class Solution2(object):
    def averageHeightOfBuildings(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        count = collections.defaultdict(lambda: (0, 0))
        for x, y, h in buildings:
            count[x] = (count[x][0]+1, count[x][1]+h)
            count[y] = (count[y][0]-1, count[y][1]-h)
        result = []
        total = cnt = 0
        prev = -1
        for curr, (c, h) in sorted(count.iteritems()):
            if cnt:
                if result and result[-1][1] == prev and result[-1][2] == total//cnt:
                    result[-1][1] = curr
                else:
                    result.append([prev, curr, total//cnt])
            total += h
            cnt += c
            prev = curr
        return result