# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: edit-distance
# source_path: LeetCode-Solutions-master/Python/edit-distance.py
# solution_class: Solution2
# submission_id: cdd106ade2b625bc99ece63cf711577f1a4274e1
# seed: 485325418

# Time:  O(n * m)
# Space: O(n + m)

class Solution2(object):
    # @return an integer
    def minDistance(self, word1, word2):
        distance = [[i] for i in xrange(len(word1) + 1)]
        distance[0] = [j for j in xrange(len(word2) + 1)]

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                insert = distance[i][j - 1] + 1
                delete = distance[i - 1][j] + 1
                replace = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                distance[i].append(min(insert, delete, replace))

        return distance[-1][-1]