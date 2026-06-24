# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-of-substrings-containing-every-vowel-and-k-consonants-i
# source_path: LeetCode-Solutions-master/Python/count-of-substrings-containing-every-vowel-and-k-consonants-i.py
# solution_class: Solution2
# submission_id: 0ae4554c9fdfce1990ea557d997d14596485ef6a
# seed: 195994026

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window, freq table

class Solution2(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        VOWELS = set("aeiou")
        def count(k):
            def update(i, d):
                if word[i] not in VOWELS:
                    curr2[0] += d
                    return
                x = ord(word[i])-ord('a')
                if cnt[x] == 0:
                    curr1[0] += 1
                cnt[x] += d
                if cnt[x] == 0:
                    curr1[0] -= 1

            result = 0
            cnt = [0]*26
            curr1, curr2 = [0], [0]
            left = 0
            for right in xrange(len(word)):
                update(right, +1)
                while curr1[0] == len(VOWELS) and curr2[0] >= k:
                    result += len(word)-right
                    update(left, -1)
                    left += 1
            return result

        return count(k)-count(k+1)