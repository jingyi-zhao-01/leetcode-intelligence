# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-string-k-special
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-string-k-special.py
# solution_class: Solution2
# submission_id: ac3fd7db0ccad37d5726744d1e17abf6a5d53ab6
# seed: 4051886891

# Time:  O(n + 26)
# Space: O(n + 26)

# freq table, counting sort, two pointers

class Solution2(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnt = [0]*26
        for x in word:
            cnt[ord(x)-ord('a')] += 1
        arr = sorted(x for x in cnt if x)
        result = float("inf")
        right = prefix = 0
        suffix = len(word)
        prev = -1
        for left in xrange(len(arr)):
            if left+1 < len(arr) and arr[left+1] == arr[left]:
                continue
            while right < len(arr) and arr[right] <= arr[left]+k:
                suffix -= arr[right]
                right += 1
            result = min(result, prefix+(suffix-(arr[left]+k)*(len(arr)-right)))
            prefix += arr[left]*(left-prev)
            prev = left
        return result