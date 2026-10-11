# Word and Character Counter

> **Task 11: Create a Word and Character Counter**  
> A beginner-level text analysis program in Python that analyzes a paragraph and calculates character counts (with and without spaces), word counts, sentence counts, and space counts.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements & Installation](#requirements--installation)
- [How to Run](#how-to-run)
- [Sample Paragraph & Statistics](#sample-paragraph--statistics)
- [Example Input & Output](#example-input--output)
- [Core Concepts & Notes](#core-concepts--notes)
  - [1. What `split()` Does](#1-what-split-does)
  - [2. `len()` vs `str.count()`](#2-len-vs-strcount)
  - [3. How Strings Are Represented in Python](#3-how-strings-are-represented-in-python)
- [Running Unit Tests](#running-unit-tests)
- [Git Setup & GitHub Push Instructions](#git-setup--github-push-instructions)

---

## Overview

Text processing is one of the foundational skills in computer programming. The **Word and Character Counter** is designed to demonstrate clean, idiomatic string manipulation and text analysis using only Python's standard library.

The program allows users to either type/paste their own paragraphs or load a built-in sample text, producing a clean, tabular statistics report.

---

## Features

- **Character Counting**:
  - `total_characters`: Measures total string length including whitespace and punctuation.
  - `characters_no_spaces`: Measures characters excluding space characters (`' '`).
- **Word Counting**:
  - Uses Python's native `str.split()` method, cleanly handling irregular whitespace and multi-space gaps.
- **Sentence Counting**:
  - Recognizes sentence endings: `.`, `!`, and `?`.
  - Handles consecutive punctuation marks like `...` (ellipses) or `?!` (interrobang) as a single sentence delimiter.
  - Correctly counts trailing sentences even if terminal punctuation was omitted.
  - Ignores leading punctuation and empty chunks.
- **Space Counting**:
  - Accurately counts space characters (`' '`) using `str.count(' ')`.
- **Friendly Edge Case Handling**:
  - Gracefully handles empty input (`""`) and whitespace-only input (`"   "`) by displaying a friendly notice and returning all counts as `0` instead of crashing.
- **Interactive Menu Loop**:
  - Lets the user choose between entering their own text or loading a built-in sample paragraph.
  - Runs in a continuous loop until the user chooses to exit.

---

## Project Structure

```
word-character-counter/
├── main.py                # Core application with analysis functions and interactive CLI
├── sample_paragraph.txt   # Built-in sample paragraph with varied punctuation
├── test_main.py           # Comprehensive unittest suite
├── .gitignore             # Python-specific git ignore file
└── README.md              # Project documentation and conceptual notes
```

---

## Requirements & Installation

- **Python**: Python 3.10+ (tested with Python 3.14)
- **Dependencies**: None! Built purely using the Python standard library (`re`, `pathlib`, `unittest`).

No `pip install` or external virtual environment packages are required.

---

## How to Run

Clone or navigate to the project directory, then run `main.py`:

```bash
python main.py
```

### Running the Test Suite

Run the unit test suite using `unittest`:

```bash
python test_main.py -v
```

or via the module runner:

```bash
python -m unittest test_main.py
```

---

## Sample Paragraph & Statistics

The project includes a built-in sample paragraph stored in `sample_paragraph.txt`:

```text
Welcome to the word and character counter project! Have you ever wondered how computers analyze human language? Python makes text manipulation simple, elegant, and fun. Is text processing really this straightforward?! Try typing your own sentences to see what you discover...
```

### Breakdown of Sentences in Sample Paragraph:
1. `Welcome to the word and character counter project!` *(ends with `!`)*
2. `Have you ever wondered how computers analyze human language?` *(ends with `?`)*
3. `Python makes text manipulation simple, elegant, and fun.` *(ends with `.`)*
4. `Is text processing really this straightforward?!` *(ends with consecutive punctuation `?!`)*
5. `Try typing your own sentences to see what you discover...` *(ends with ellipsis `...`)*

### Calculated Statistics for the Sample Paragraph:

| Metric | Count | Explanation |
| :--- | :---: | :--- |
| **Total Characters (with spaces)** | **275** | `len(text)` including all characters |
| **Characters (without spaces)** | **235** | Total characters minus space characters |
| **Words** | **41** | Words extracted using `split()` |
| **Sentences** | **5** | Sentences identified by `.`, `!`, `?`, `?!`, and `...` |
| **Spaces** | **40** | Total `' '` characters |

---

## Example Input & Output

### 1. Analyzing the Built-in Sample Paragraph (Option 2)

```text
============================================
      WORD AND CHARACTER COUNTER
============================================

Please choose an option:
  1. Type or paste your own paragraph
  2. Use built-in sample paragraph
  3. Exit

Enter choice (1-3): 2

--- Built-in Sample Paragraph ---
Welcome to the word and character counter project! Have you ever wondered how computers analyze human language? Python makes text manipulation simple, elegant, and fun. Is text processing really this straightforward?! Try typing your own sentences to see what you discover...
---------------------------------

============================================
           TEXT ANALYSIS REPORT
============================================
  Total Characters (with spaces):       275
  Characters (without spaces):          235
  Words:                                 41
  Sentences:                              5
  Spaces:                                40
============================================
```

### 2. Typing Custom Text with Varied Punctuation (Option 1)

**User Input:**
```text
Python is amazing. Don't you think?
```

**Output:**
```text
============================================
           TEXT ANALYSIS REPORT
============================================
  Total Characters (with spaces):        35
  Characters (without spaces):           30
  Words:                                  6
  Sentences:                              2
  Spaces:                                 5
============================================
```

### 3. Handling Empty or Whitespace-Only Input

**User Input:** (Pressing Enter immediately or typing spaces)

**Output:**
```text
[Notice] Input is empty or contains only whitespace. All counts are 0.

============================================
           TEXT ANALYSIS REPORT
============================================
  Total Characters (with spaces):         0
  Characters (without spaces):            0
  Words:                                  0
  Sentences:                              0
  Spaces:                                 0
============================================
```

---

## Core Concepts & Notes

### 1. What `split()` Does

In Python, `str.split()` splits a string into a list of substrings. When called **without arguments** (`text.split()`):

```python
words = text.split()
```

- **Whitespace Delimiter**: It treats any sequence of consecutive whitespace characters (spaces `' '`, tabs `'\t'`, and newlines `'\n'`) as a single delimiter.
- **Automatic Trimming**: Unlike `text.split(' ')`, `text.split()` automatically strips leading and trailing whitespace.
- **Multiple Spaces**: Multiple spaces between words do not produce empty strings in the output:
  ```python
  "Hello      world".split()    # ['Hello', 'world'] -> len == 2
  "Hello      world".split(" ") # ['Hello', '', '', '', '', '', 'world'] -> len == 7
  ```
- **Word Counting**: Calling `len(text.split())` gives an accurate, clean word count without needing complex regexes.

---

### 2. `len()` vs `str.count()`

While both functions measure string properties, their mechanics and use cases are distinct:

| Feature | `len(s)` | `s.count(sub)` |
| :--- | :--- | :--- |
| **Type** | Built-in function (`len(...)`) | String method (`str.count(...)`) |
| **Purpose** | Measures the total number of characters in the string | Counts non-overlapping occurrences of a specific substring `sub` |
| **Time Complexity** | **$\mathcal{O}(1)$** (instant) | **$\mathcal{O}(N)$** (linear scan) |
| **How it Works** | Python string objects store their length in internal memory headers (in C struct `PyASCIIObject`). Calling `len()` simply reads that value. | Scans through the sequence character-by-character to locate and count occurrences of `sub`. |
| **Example** | `len("cat")` $\rightarrow$ `3` | `"banana".count("an")` $\rightarrow$ `2` |

In our counter:
- `len(text)` returns total characters in $\mathcal{O}(1)$ time.
- `text.count(" ")` scans the string to return the exact number of space characters.
- Subtracting them (`len(text) - text.count(" ")`) gives the exact number of characters excluding spaces.

---

### 3. How Strings Are Represented in Python

Python strings (`str`) have several key characteristics:

1. **Immutability**:
   - Once created, a Python string cannot be modified in-place.
   - Operations like `.replace()`, `.strip()`, or `+` create a brand-new string object in memory. This guarantees thread safety and hashability (allowing strings to be dictionary keys and set elements).

2. **Unicode Sequences**:
   - In Python 3, all strings are sequences of Unicode code points. Characters can range from ASCII letters (`A-Z`) to accented characters (`é`), non-Latin scripts (`한`, `Ω`), and emojis (`🚀`).

3. **PEP 393 - Flexible String Representation**:
   - To save memory without sacrificing full Unicode support, Python dynamically chooses the most compact internal byte representation:
     - **Latin-1 (1 byte per char)**: Used if all characters fit in ASCII / ISO-8859-1 (code points $\le 255$).
     - **UCS-2 (2 bytes per char)**: Used if characters fit in the Basic Multilingual Plane (code points $\le 65,535$).
     - **UCS-4 (4 bytes per char)**: Used if supplementary characters/emojis are present (code points $\le 1,114,111$).
   - This ensures $\mathcal{O}(1)$ random access by index (`s[i]`) while keeping memory usage minimal.

---

## Running Unit Tests

The test suite in [test_main.py](file:///C:/Users/HEMA/.gemini/antigravity/scratch/word-character-counter/test_main.py) tests all requirements and edge cases:

1. **`test_normal_paragraph`**: Tests full paragraph metrics against manual calculations.
2. **`test_empty_string`**: Ensures empty strings return zeros across all metrics without crashing.
3. **`test_only_spaces`**: Verifies whitespace-only strings return zeroed statistics.
4. **`test_multiple_spaces_between_words`**: Ensures extra spaces do not inflate word counts.
5. **`test_consecutive_punctuation`**: Verifies `...` and `?!` count as single sentence boundaries.
6. **`test_no_ending_punctuation`**: Verifies unpunctuated sentences and hanging trailing clauses.
7. **`test_sample_paragraph_file`**: Validates `sample_paragraph.txt` contents against expected values.
8. **`test_format_report`**: Confirms output formatting and report table structure.

Execute the tests with:
```bash
python test_main.py -v
```

---

## Git Setup & GitHub Push Instructions

Follow these commands to push this repository to your GitHub account:

```bash
# 1. Navigate to the project directory
cd C:\Users\HEMA\.gemini\antigravity\scratch\word-character-counter

# 2. Check git status
git status

# 3. Add your remote origin (if not already added)
git remote add origin https://github.com/hemasrimalla/word-character-counter.git

# 4. Set the default branch to main and push
git branch -M main
git push -u origin main
```

*(If the remote already exists, you can verify with `git remote -v` or update it with `git remote set-url origin https://github.com/hemasrimalla/word-character-counter.git`)*
