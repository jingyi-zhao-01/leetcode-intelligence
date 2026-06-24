# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pyramid-transition-matrix
# source_path: LeetCode-Solutions-master/Python/pyramid-transition-matrix.py
# solution_class: Solution
# submission_id: 796847fe44733717dab68e90814fa69901badb5f
# seed: 3685841282

# Time:  O((a^(b+1)-a)/(a-1)) = O(a^b) , a is the size of allowed,
#                                        b is the length of bottom
# Space: O((a^(b+1)-a)/(a-1)) = O(a^b)

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def pyramidTransitionHelper(bottom, edges, lookup):
            def dfs(bottom, edges, new_bottom, idx, lookup):
                if idx == len(bottom)-1:
                    return pyramidTransitionHelper("".join(new_bottom), edges, lookup)
                for i in edges[ord(bottom[idx])-ord('A')][ord(bottom[idx+1])-ord('A')]:
                    new_bottom[idx] = chr(i+ord('A'))
                    if dfs(bottom, edges, new_bottom, idx+1, lookup):
                        return True
                return False

            if len(bottom) == 1:
                return True
            if bottom in lookup:
                return False
            lookup.add(bottom)
            for i in xrange(len(bottom)-1):
                if not edges[ord(bottom[i])-ord('A')][ord(bottom[i+1])-ord('A')]:
                    return False
            new_bottom = ['A']*(len(bottom)-1)
            return dfs(bottom, edges, new_bottom, 0, lookup)

        edges = [[[] for _ in xrange(7)] for _ in xrange(7)]
        for s in allowed:
            edges[ord(s[0])-ord('A')][ord(s[1])-ord('A')].append(ord(s[2])-ord('A'))
        return pyramidTransitionHelper(bottom, edges, set())