# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-possible-recipes-from-given-supplies
# source_path: LeetCode-Solutions-master/Python/find-all-possible-recipes-from-given-supplies.py
# solution_class: Solution
# submission_id: d76d42d843f728d9eff140669538a2759d63ed99
# seed: 2972873968

# Time:  O(|E|)
# Space: O(|E|)

import collections
import itertools

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        indegree = collections.defaultdict(int)
        adj = collections.defaultdict(list)
        for r, ingredient in itertools.izip(recipes, ingredients): 
            indegree[r] = len(ingredient)
            for ing in ingredient:
                adj[ing].append(r)
        result = []
        recipes = set(recipes)
        q = supplies
        while q: 
            new_q = []
            for u in q:
                if u in recipes:
                    result.append(u)
                for v in adj[u]:
                    indegree[v] -= 1
                    if not indegree[v]:
                        new_q.append(v)
            q = new_q
        return result 