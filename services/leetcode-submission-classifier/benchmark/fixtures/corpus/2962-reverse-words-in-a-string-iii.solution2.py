# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-in-a-string-iii
# source_path: LeetCode-Solutions-master/Python/reverse-words-in-a-string-iii.py
# solution_class: Solution2
# submission_id: 4088be7bdef2e0186b5d44539d7aa7571f62163f
# seed: 4238388306

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def reverseWords(self, s):
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)