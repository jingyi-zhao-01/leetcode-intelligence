# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-prefix-of-k-strings-after-removal
# source_path: LeetCode-Solutions-master/Python/longest-common-prefix-of-k-strings-after-removal.py
# solution_class: Solution
# submission_id: e6d265efcb4ff956e286e0491d07cb79a608895e
# seed: 1808604542

# Time:  O(l * nlogn)
# Space: O(n)

# sort, sliding window, prefix sum

class Solution(object):
    def longestCommonPrefix(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[int]
        """
        idxs = range(len(words))
        idxs.sort(key=lambda x: words[x])
        def longest_common_prefix(k):
            lcp = [0]*len(words)
            for i in xrange(len(words)-(k-1)):
                left = words[idxs[i]]
                right = words[idxs[i+(k-1)]]
                l = min(len(left), len(right))
                lcp[i] = next((j for j in xrange(l) if left[j] != right[j]), l)
            return lcp
        
        lcp = longest_common_prefix(k)
        prefix = [0]*len(words)
        prefix[0] = lcp[0]
        for i in xrange(len(prefix)-1):
            prefix[i+1] = max(prefix[i], lcp[i+1])
        suffix = [0]*len(words)
        suffix[-1] = lcp[-1]
        for i in reversed(xrange(len(suffix)-1)):
            suffix[i] = max(suffix[i+1], lcp[i])
        result = [0]*len(words)
        mx = max(longest_common_prefix(k+1))
        for i in xrange(len(words)):
            idx = idxs[i]
            mx1 = prefix[i-k] if i-k >= 0 else 0
            mx2 = suffix[i+1] if i+1 < len(words) else 0
            result[idx] = max(mx, mx1, mx2)
        return result