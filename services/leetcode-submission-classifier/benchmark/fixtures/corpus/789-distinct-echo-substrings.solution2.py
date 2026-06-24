# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distinct-echo-substrings
# source_path: LeetCode-Solutions-master/Python/distinct-echo-substrings.py
# solution_class: Solution2
# submission_id: f928363d13cfcf3b121fdffd4beace499af8076a
# seed: 3504107881

# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set

class Solution2(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        result = set()
        for l in xrange(1, len(text)//2+1):
            count = sum(text[i] == text[i+l] for i in xrange(l))
            for i in xrange(len(text)-2*l):
                if count == l:
                    result.add(text[i:i+l])
                count += (text[i+l] == text[i+l+l]) - (text[i] == text[i+l])
            if count == l:
                result.add(text[len(text)-2*l:len(text)-2*l+l])
        return len(result)