# FLA Task 3: Pushdown Automata (PDA) & CFG Applications

This repository features Python-based simulations of Pushdown Automata (PDA) for validating balanced brackets and hierarchical structures, alongside validation logic demonstrating Context-Free Grammars (CFG) / Regular expressions for Roman numerals.

## Features

1. **Balanced Brackets PDA (`balanced_brackets.py`)**
   - Employs a stack-based PDA architecture to check nested matching structures containing `()`, `[]`, and `{}`.

2. **XML Tag Matching PDA (`xml_tag_matching.py`)**
   - Implements a stack mechanism to validate matching hierarchical HTML/XML tags, with complete support for self-closing tags (e.g., `<input />`).

3. **Roman Numeral CFG/DFA (`roman_numerals.py`)**
   - Implements validation of standard Roman numerals (up to 3999) using pattern definitions modeling context-free rules.

## Project Structure
```
├── balanced_brackets.py     # Balanced bracket matching PDA
├── xml_tag_matching.py      # XML open/close tag parser PDA
├── roman_numerals.py        # Roman numeral CFG/DFA logic
├── test_cases.py            # Standard test suite
├── main.py                  # CLI executable to verify code
└── README.md                # Project documentation
```

## Running the Program
To execute the verification suite:
```bash
python main.py
