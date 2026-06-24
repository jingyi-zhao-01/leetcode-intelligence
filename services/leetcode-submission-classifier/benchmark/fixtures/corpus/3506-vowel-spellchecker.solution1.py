# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: vowel-spellchecker
# source_path: LeetCode-Solutions-master/Python/vowel-spellchecker.py
# solution_class: Solution
# submission_id: d676659d6657388d7e8ad39f700b22883e73dd2a
# seed: 758883887

# Time:  O(n)
# Space: O(w)

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        def todev(word):
            return "".join('*' if c.lower() in vowels else c.lower()
                           for c in word)

        words = set(wordlist)
        caps = {}
        vows = {}

        for word in wordlist:
            caps.setdefault(word.lower(), word)
            vows.setdefault(todev(word), word)

        def check(query):
            if query in words:
                return query
            lower = query.lower()
            if lower in caps:
                return caps[lower]
            devow = todev(lower)
            if devow in vows:
                return vows[devow]
            return ""
        return map(check, queries)