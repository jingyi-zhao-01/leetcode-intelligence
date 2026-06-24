# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reconstruct-itinerary
# source_path: LeetCode-Solutions-master/Python/reconstruct-itinerary.py
# solution_class: Solution2
# submission_id: e5fcc9e16b693e75fc2f1409fdd91141e667b906
# seed: 2584718786

# Time:  O(|V| + |E|log|V|)
# Space: O(|V| + |E|)

# Hierholzer Algorithm
import collections

class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def route_helper(origin, ticket_cnt, graph, ans):
            if ticket_cnt == 0:
                return True

            for i, (dest, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    ans.append(dest)
                    if route_helper(dest, ticket_cnt - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        for k in graph.keys():
            graph[k].sort()

        origin = "JFK"
        ans = [origin]
        route_helper(origin, len(tickets), graph, ans)
        return ans