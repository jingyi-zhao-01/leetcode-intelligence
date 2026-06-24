# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
# source_path: LeetCode-Solutions-master/Python/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list.py
# solution_class: Solution2
# submission_id: 8e211db29cb6e3f03d94086bb762e641aacff77e
# seed: 214036298

# Time:  O(n * m * l + n^2 * m), n is favoriteCompanies.length
#                              , m is the max of favoriteCompanies[i].length
#                              , l is the max of favoriteCompanies[i][j].length
# Space: O(n * m * l)

class Solution2(object):
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
        union_find = UnionFind(comps)
        for i in xrange(len(comps)):
            for j in xrange(len(comps)):
                if j == i:
                    continue
                union_find.union_set(i, j)
        return [x for i, x in enumerate(union_find.set) if x == i]