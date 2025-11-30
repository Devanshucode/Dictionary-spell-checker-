# Dictionary-spell-checker-
This project is a simple yet powerful Spell Checker implemented using the Trie (Prefix Tree) data structure.
It allows you to:

✔ Insert words into a Trie
✔ Search for valid words
✔ Provide auto-complete style suggestions
✔ Check user input for spelling errors

This makes it ideal for beginners learning data structures, or for anyone building a lightweight dictionary/spell-checking tool.

🚀 Features
🔡 Trie Data Structure

Efficient insertion and search operations with O(n) time complexity.

✔ Spell Checking

Checks if a given word is spelled correctly.

💡 Word Suggestions

If a word is incorrect, it suggests possible correct words based on the first two letters.

📥 Dictionary Loading

You can load words from:

A Python list

A text file (optional and easily extendable)

🎮 Interactive CLI

User can type words to check spelling continuously until they type "exit".

📂 Project Structure
spell_checker/
│
├── trie.py            # Trie class and node implementation
├── spell_checker.py   # Spell check logic + dictionary loading
├── dictionary.txt      # (Optional) Word list file
└── README.md          # Project documentation
🧠 How It Works

1. Each word from the dictionary is inserted into a Trie.

2. When the user enters a word:

The program checks if it exists in the Trie.

If not, it generates suggestions using depth-first search (DFS) starting from the word’s prefix.


OUTPUT:

<img width="1061" height="322" alt="image" src="https://github.com/user-attachments/assets/5aaf798e-5a4c-456e-8791-26dd7fd9fb3e" />


Feel free to submit pull requests or open issues if you want to improve this project!
