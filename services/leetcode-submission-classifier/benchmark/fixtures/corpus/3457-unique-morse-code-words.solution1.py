# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-morse-code-words
# source_path: LeetCode-Solutions-master/Python/unique-morse-code-words.py
# solution_class: Solution
# submission_id: 6d544263a25d6a396736fb86c28793f2e2524216
# seed: 3640664036

# Time:  O(n), n is the sume of all word lengths
# Space: O(n)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        lookup = {"".join(MORSE[ord(c) - ord('a')] for c in word) \
                  for word in words}
        return len(lookup)