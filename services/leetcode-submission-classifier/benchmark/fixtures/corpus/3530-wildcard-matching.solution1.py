# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wildcard-matching
# source_path: LeetCode-Solutions-master/Python/wildcard-matching.py
# solution_class: Solution
# submission_id: 2bd49533c9d8dedb79516d230777a62af3101c00
# seed: 1894365836

# Time:  O(m + n) ~ O(m * n)
# Space: O(1)

# iterative solution with greedy

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        count = 0  # used for complexity check
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_p_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                assert(count <= (len(p)+1) * (len(s)+1))
                return False
            count += 1  # used for complexity check
 
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            count += 1  # used for complexity check

        assert(count <= (len(p)+1) * (len(s)+1))
        return p_ptr == len(p)