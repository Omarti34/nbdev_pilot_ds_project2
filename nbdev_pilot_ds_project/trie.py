# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_trie.ipynb.

# %% auto 0
__all__ = ['TrieNode', 'Trie']

# %% ../nbs/01_trie.ipynb 3
class TrieNode:
    "Stores the hashtable of the letters and tells if that node is the end of a word."
    def __init__(self) -> None:
        self.end = False
        self.letters = {}

# %% ../nbs/01_trie.ipynb 4
class Trie:
    "Trie data structure. Can store multiple words in a graph linking each consecutive letters and make branches in them."
    def __init__(self) -> None:
        self.head = TrieNode()
    def insert(self, 
            word: str # word to store in the trie
            ) -> bool: 
        actual_iteration = self.head
        for letter in word:
            actual_iteration_letters = actual_iteration.letters
            if not letter in actual_iteration_letters:
                actual_iteration_letters[letter] = TrieNode()
            actual_iteration=actual_iteration_letters[letter]
        actual_iteration.end = True
        return True
