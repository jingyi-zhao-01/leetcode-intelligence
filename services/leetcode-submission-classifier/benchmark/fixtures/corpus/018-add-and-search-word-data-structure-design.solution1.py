# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-and-search-word-data-structure-design
# source_path: LeetCode-Solutions-master/Python/add-and-search-word-data-structure-design.py
# solution_class: Solution
# submission_id: ab5ead5bc7bc52a1c5e55ebd857977caad8a82aa
# seed: 2072385493

# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        elif word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start+1, curr.leaves[c]):
                    return True

        return False


