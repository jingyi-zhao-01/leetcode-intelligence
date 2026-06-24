# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-with-same-vowel-count
# source_path: LeetCode-Solutions-master/Python/reverse-words-with-same-vowel-count.py
# solution_class: Solution2
# submission_id: 22471a67564ec2c4081a7bd320ddf31683b1490a
# seed: 4204861696

# Time:  O(n)
# Space: O(1)

# string, inplace

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = set("aeiou")
        def count(s):
            return sum(x in VOWELS for x in s)

        result = s.split()
        cnt = count(result[0])
        return " ".join(w if not i or count(w) != cnt else w[::-1] for i, w in enumerate(result))