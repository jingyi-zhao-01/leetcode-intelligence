# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-k-length-substrings-with-no-repeated-characters
# source_path: LeetCode-Solutions-master/Python/find-k-length-substrings-with-no-repeated-characters.py
# solution_class: Solution
# submission_id: 44da2c675ec388ae62fb94a97512de4a666b5cc6
# seed: 3551251377

# Time:  O(n)
# Space: O(k)

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        result, i = 0, 0
        lookup = set()
        for j in xrange(len(S)):
            while S[j] in lookup:
                lookup.remove(S[i])
                i += 1
            lookup.add(S[j])
            result += j-i+1 >= K
        return result