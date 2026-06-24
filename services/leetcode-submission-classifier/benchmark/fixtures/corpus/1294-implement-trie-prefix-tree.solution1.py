# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-trie-prefix-tree
# source_path: LeetCode-Solutions-master/Python/implement-trie-prefix-tree.py
# solution_class: Solution
# submission_id: d8f1240f5fe37cb1eb5ae4c3a4dcca1000abfbe3
# seed: 383765004

# Time:  O(n), per operation
# Space: O(1)

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur


