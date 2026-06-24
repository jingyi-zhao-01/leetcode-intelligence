# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-with-at-most-two-distinct-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-with-at-most-two-distinct-characters.py
# solution_class: Solution
# submission_id: 172e8f0544fb938fa2692e3ccf78a30004431c10
# seed: 3417772130

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1
            while distinct_count > 2:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1
            longest = max(longest, i - start + 1)
        return longest