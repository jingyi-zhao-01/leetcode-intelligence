# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reconstruct-itinerary
# source_path: LeetCode-Solutions-master/Python/reconstruct-itinerary.py
# solution_class: Solution
# submission_id: 9ca20cf32ec3fb6c58726a4404cae213b1d02301
# seed: 3115793169

# Time:  O(|V| + |E|log|V|)
# Space: O(|V| + |E|)

# Hierholzer Algorithm
import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = collections.defaultdict(list)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        for x in adj.itervalues():
            x.sort(reverse=True)
        origin = "JFK"
        result = []
        stk = [origin]
        while stk:
            while adj[stk[-1]]: 
                stk.append(adj[stk[-1]].pop())
            result.append(stk.pop())
        result.reverse()
        return result