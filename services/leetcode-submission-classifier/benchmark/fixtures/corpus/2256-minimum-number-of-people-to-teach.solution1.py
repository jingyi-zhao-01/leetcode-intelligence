# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-people-to-teach
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-people-to-teach.py
# solution_class: Solution
# submission_id: 48a7c73b901dda8057e47f329b1ef4168f8162f7
# seed: 72870819

# Time:  O(n * m^2)
# Space: O(n * m)

import collections

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        language_sets = map(set, languages)  # Space: O(m * n)
        candidates = set(i-1 for u, v in friendships if not language_sets[u-1] & language_sets[v-1] for i in [u, v])  # Time: O(m^2 * n), Space: O(m)
        count = collections.Counter()
        for i in candidates:  # Time: O(m * n)
            count += collections.Counter(languages[i])
        return len(candidates) - max(count.values() + [0])