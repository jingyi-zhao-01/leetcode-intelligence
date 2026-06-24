# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-coins-heroes-can-collect
# source_path: LeetCode-Solutions-master/Python/maximum-coins-heroes-can-collect.py
# solution_class: Solution
# submission_id: 8af4db9a81a6317a7e02a7ac0a9c53a85996fb3f
# seed: 3636525764

# Time:  O(nlogn + mlogm)
# Space: O(n + m)

# sort, two pointers

class Solution(object):
    def maximumCoins(self, heroes, monsters, coins):
        """
        :type heroes: List[int]
        :type monsters: List[int]
        :type coins: List[int]
        :rtype: List[int]
        """
        idxs1 = range(len(heroes))
        idxs1.sort(key=lambda x: heroes[x])
        idxs2 = range(len(monsters))
        idxs2.sort(key=lambda x: monsters[x])
        result = [0]*len(idxs1)
        i = curr = 0
        for idx in idxs1:
            for i in xrange(i, len(idxs2)):
                if monsters[idxs2[i]] > heroes[idx]:
                    break
                curr += coins[idxs2[i]]
            else:
                i = len(idxs2)
            result[idx] = curr
        return result