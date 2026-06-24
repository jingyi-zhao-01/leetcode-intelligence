# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
# source_path: LeetCode-Solutions-master/Python/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list.py
# solution_class: Solution
# submission_id: 1b8e3a5c321f54523cfc8be0c6960316f960acb0
# seed: 2654641617

# Time:  O(n * m * l + n^2 * m), n is favoriteCompanies.length
#                              , m is the max of favoriteCompanies[i].length
#                              , l is the max of favoriteCompanies[i][j].length
# Space: O(n * m * l)

class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        lookup, comps = {}, []
        for cs in favoriteCompanies:
            comps.append(set())
            for c in cs:
                if c not in lookup:
                    lookup[c] = len(lookup)
                comps[-1].add(lookup[c])
        return [i for i, c1 in enumerate(comps)
                if not any(i != j and len(c1) < len(c2) and c1 < c2
                           for j, c2 in enumerate(comps))]