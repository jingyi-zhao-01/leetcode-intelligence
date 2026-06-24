# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-close-characters
# source_path: LeetCode-Solutions-master/Python/merge-close-characters.py
# solution_class: Solution2
# submission_id: b46b3ccb91a3da1f962914fa6d2ad08c1a8daa73
# seed: 1341585253

# Time:  O(n + 26)
# Space: O(26)

# simulation, hash table

class Solution2(object):
    def mergeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        cnt = [0]*26
        for x in s:
            if cnt[ord(x)-ord('a')]:
                continue
            cnt[ord(x)-ord('a')] += 1
            result.append(x)
            if len(result) >= k+1:
                cnt[ord(result[-(k+1)])-ord('a')] -= 1
        return "".join(result)