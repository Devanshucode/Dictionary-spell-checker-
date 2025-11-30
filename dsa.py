class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the Trie
    def search(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Suggest similar words (auto-complete style)
    def suggest(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._dfs(node, prefix.lower(), suggestions)
        return suggestions

    def _dfs(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, suggestions)


# ---------------------------
# Spell Checker Using Trie
# ---------------------------
def load_dictionary(trie, word_list):
    for word in word_list:
        trie.insert(word)

def spell_check(trie, word):
    if trie.search(word):
        print(f"✅ '{word}' is spelled correctly.")
    else:
        print(f"❌ '{word}' not found in dictionary.")
        suggestions = trie.suggest(word[:2])  # Suggest words starting with same first 2 letters
        if suggestions:
            print("💡 Did you mean:", ", ".join(suggestions[:5]))
        else:
            print("No suggestions found.")


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    # You can load from a file instead of a list
    english_words = ["apple", "banana", "grape", "orange", "mango", "watermelon", "pineapple"]

    trie = Trie()
    load_dictionary(trie, english_words)

    while True:
        word = input("\nEnter a word to spell check (or 'exit' to quit): ").strip()
        if word.lower() == "exit":
            break
        spell_check(trie, word)
