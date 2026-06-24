# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distinct-echo-substrings
# source_path: LeetCode-Solutions-master/Python/distinct-echo-substrings.py
# solution_class: Solution
# submission_id: 0256cf962886549a9efe95e3702dee8379fba7ae
# seed: 1406281888

# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set

class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        def KMP(text, l, result):
            prefix = [-1]*(len(text)-l)
            j = -1
            for i in xrange(1, len(prefix)):
                while j > -1 and text[l+j+1] != text[l+i]:
                    j = prefix[j]
                if text[l+j+1] == text[l+i]:
                    j += 1
                prefix[i] = j
                if (j+1) and (i+1) % ((i+1) - (j+1)) == 0 and \
                   (i+1) // ((i+1) - (j+1)) % 2 == 0:
                    result.add(text[l:l+i+1])
            return len(prefix)-(prefix[-1]+1) \
                   if prefix[-1]+1 and len(prefix) % (len(prefix)-(prefix[-1]+1)) == 0 \
                   else float("inf")

        result = set()
        i, l = 0, len(text)-1
        while i < l:  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefabcdefabcdef
            l = min(l, i + KMP(text, i, result))
            i += 1
        return len(result)