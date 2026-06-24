# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nodes-with-the-highest-score
# source_path: LeetCode-Solutions-master/Python/count-nodes-with-the-highest-score.py
# solution_class: Solution2
# submission_id: 26f945a10d4ac5afed1b8771eb8abc5d8fbba470
# seed: 1567556228

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        def dfs(adj, i, result):
            cnts = [dfs(adj, child, result) for child in adj[i]]
            total = sum(cnts)+1
            score = max((len(adj)-total), 1)*reduce(lambda x, y: x*y, cnts, 1)
            if score > result[0]:
                result[:] = [score, 1]
            elif score == result[0]:
                result[1] += 1
            return total

        adj = [[] for _ in xrange(len(parents))]  # Space: O(n)
        for i in xrange(1, len(parents)):
            adj[parents[i]].append(i)
        result = [0]*2
        dfs(adj, 0, result)
        return result[1]