#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""字典树"""


class Trie:

    class Node:
        def __init__(self, data):
            self.data = data
            self.children = [None] * 26
            self.is_end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node('/')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if p.children[index] is None:
                p.children[index] = self.Node(c)
            p = p.children[index]
        p.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if p.children[index] is None:
                return False
            else:
                p = p.children[index]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if p.children[index] is None:
                return False
            else:
                p = p.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print(obj.search('app'))
    print(obj.startsWith('applee'))
