"""
Word and Character Counter (Task 11)
------------------------------------
A beginner-friendly text analysis tool that calculates:
- Total characters (with and without spaces)
- Words (using str.split())
- Sentences (counting ., !, ? with consecutive punctuation and trailing sentences)
- Spaces (using str.count(' '))

Built using only the Python standard library.
"""

from pathlib import Path
import re


def count_characters(text: str) -> tuple[int, int]:
    """
    Count total characters and characters excluding space characters.

    Parameters:
        text (str): The input string to measure.

    Returns:
        tuple[int, int]: (total_characters, characters_without_spaces)
    """
    total = len(text)
    without_spaces = len(text.replace(" ", ""))
    return total, without_spaces


def count_words(text: str) -> int:
    """
    Count the number of words in the text using split().

    str.split() with no arguments splits on arbitrary sequences of whitespace
    (spaces, tabs, newlines) and automatically ignores leading/trailing whitespace.

    Parameters:
        text (str): The input string.

    Returns:
        int: Number of words.
    """
    return len(text.split())


def count_sentences(text: str) -> int:
    """
    Count sentences in text based on sentence endings (. ! ?).

    Rules:
    - Counts sentence endings: '.', '!', '?'.
    - Handles consecutive punctuation like '...' or '?!' as a single ending.
    - Counts a trailing sentence even if it has no final punctuation.
    - Returns 0 for empty or whitespace-only input.

    Parameters:
        text (str): The input string.

    Returns:
        int: Number of sentences.
    """
    cleaned = text.strip()
    if not cleaned:
        return 0

    # Split on one or more consecutive sentence-ending punctuation marks (. ! ?)
    # E.g. '...', '?!', '!!' are treated as a single delimiter.
    parts = re.split(r"[.!?]+", cleaned)

    # Filter out empty chunks (such as from leading punctuation or split artifacts).
    # Chunks preceding punctuation marks represent punctuated sentences.
    # An unpunctuated trailing sentence appears as the last non-empty chunk.
    sentences = [part.strip() for part in parts if part.strip()]
    return len(sentences)


def count_spaces(text: str) -> int:
    """
    Count the number of space characters (' ') in the text.

    Parameters:
        text (str): The input string.

    Returns:
        int: Count of ' ' characters.
    """
    return text.count(" ")


def analyze_text(text: str) -> dict:
    """
    Analyze text and return comprehensive statistics as a dictionary.

    If text is empty or contains only whitespace, returns all counts as 0
    without raising an error.

    Parameters:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary containing:
            - total_characters: Total character count (including spaces)
            - characters: Alias for total_characters
            - characters_no_spaces: Total characters excluding space characters
            - words: Total word count
            - sentences: Total sentence count
            - spaces: Total space character count
    """
    # Requirement 2: Handle empty input and whitespace-only input (all counts = 0)
    if not text or not text.strip():
        return {
            "total_characters": 0,
            "characters": 0,
            "characters_no_spaces": 0,
            "words": 0,
            "sentences": 0,
            "spaces": 0,
        }

    total_chars, chars_no_spaces = count_characters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    spaces = count_spaces(text)

    return {
        "total_characters": total_chars,
        "characters": total_chars,
        "characters_no_spaces": chars_no_spaces,
        "words": words,
        "sentences": sentences,
        "spaces": spaces,
    }


def format_report(stats: dict) -> str:
    """
    Format statistics dictionary into a clean, human-readable report.

    Parameters:
        stats (dict): The dictionary returned by analyze_text.

    Returns:
        str: Formatted report table.
    """
    border = "=" * 44
    lines = [
        border,
        "           TEXT ANALYSIS REPORT",
        border,
        f"  Total Characters (with spaces):    {stats['total_characters']:>6}",
        f"  Characters (without spaces):       {stats['characters_no_spaces']:>6}",
        f"  Words:                             {stats['words']:>6}",
        f"  Sentences:                         {stats['sentences']:>6}",
        f"  Spaces:                            {stats['spaces']:>6}",
        border,
    ]
    return "\n".join(lines)


def get_user_text() -> str:
    """
    Prompt the user to enter or paste a paragraph.

    Supports both single-line and multi-line paragraphs.
    Pressing Enter on an empty line finishes input.

    Returns:
        str: The full entered text.
    """
    print("\nEnter or paste your paragraph below.")
    print("(Tip: Press Enter on an empty line when finished; press Enter immediately for empty input):")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            if not lines:
                # User pressed Enter immediately -> empty input
                return ""
            # Blank line after some text -> user finished entering
            break
        lines.append(line)
    return "\n".join(lines)


def main() -> None:
    """
    Run the main interactive Word and Character Counter program loop.
    """
    print("=" * 44)
    print("      WORD AND CHARACTER COUNTER")
    print("=" * 44)

    sample_file_path = Path(__file__).parent / "sample_paragraph.txt"

    while True:
        print("\nPlease choose an option:")
        print("  1. Type or paste your own paragraph")
        print("  2. Use built-in sample paragraph")
        print("  3. Exit")

        try:
            choice = input("\nEnter choice (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting program. Goodbye!")
            break

        if choice == "1":
            user_text = get_user_text()

            if not user_text.strip():
                print("\n[Notice] Input is empty or contains only whitespace. All counts are 0.")

            stats = analyze_text(user_text)
            print("\n" + format_report(stats))

        elif choice == "2":
            if not sample_file_path.exists():
                print(f"\n[Error] Sample file '{sample_file_path.name}' was not found.")
                continue

            try:
                with open(sample_file_path, "r", encoding="utf-8") as file:
                    sample_text = file.read().strip()
            except OSError as err:
                print(f"\n[Error] Could not read sample file: {err}")
                continue

            print("\n--- Built-in Sample Paragraph ---")
            print(sample_text.strip())
            print("-" * 33)

            stats = analyze_text(sample_text)
            print("\n" + format_report(stats))

        elif choice == "3":
            print("\nThank you for using Word and Character Counter. Goodbye!\n")
            break

        else:
            print("\n[Invalid choice] Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
