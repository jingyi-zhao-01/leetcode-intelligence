# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: robot-collisions
# source_path: LeetCode-Solutions-master/Python/robot-collisions.py
# solution_class: Solution
# submission_id: 8a32a4e664d0092e381c0330ec13f66334c88a7f
# seed: 4215889460

# Time:  O(nlogn)
# Space: O(n)

# sort, simulation, stack

class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        stk = []
        for i in sorted(xrange(len(positions)), key=lambda x:positions[x]):
            if directions[i] == 'R':
                stk.append(i)
                continue
            while stk:
                if healths[stk[-1]] == healths[i]:
                    healths[stk.pop()] = healths[i] = 0
                    break
                if healths[stk[-1]] > healths[i]:
                    healths[i] = 0
                    healths[stk[-1]] -= 1
                    break                
                healths[stk.pop()] = 0
                healths[i] -= 1
        return [x for x in healths if x]