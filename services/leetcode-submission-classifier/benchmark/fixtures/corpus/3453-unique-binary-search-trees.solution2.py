# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-binary-search-trees
# source_path: LeetCode-Solutions-master/Python/unique-binary-search-trees.py
# solution_class: Solution2
# submission_id: f0ac0fa9872e8be4943aae9a190a2eaaaa2f5a0a
# seed: 3884143276

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @return an integer
    def numTrees(self, n):
        counts = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]