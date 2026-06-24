# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-vii
# source_path: LeetCode-Solutions-master/Python/jump-game-vii.py
# solution_class: Solution2
# submission_id: 1baecf88c8620cc904604beb943e273134d05b20
# seed: 1327912046

# Time:  O(n)
# Space: O(n)

# dp with line sweep solution

class Solution2(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        q = collections.deque([0])
        reachable = 0
        while q:
            i = q.popleft()
            for j in xrange(max(i+minJump, reachable+1), min(i+maxJump+1, len(s))):
                if s[j] != '0':
                    continue
                q.append(j)
            reachable = i+maxJump
        return i == len(s)-1