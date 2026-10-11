"""
Unit tests for Word and Character Counter (main.py).

Covers:
1. Normal paragraph
2. Empty string
3. Only spaces
4. Multiple spaces between words
5. Text with '...' and '?!'
6. Text with no ending punctuation
7. Built-in sample paragraph verification
"""

from pathlib import Path
import unittest

from main import (
    analyze_text,
    count_characters,
    count_sentences,
    count_spaces,
    count_words,
    format_report,
)


class TestWordCharacterCounter(unittest.TestCase):
    """Test suite covering text analysis functions in main.py."""

    def test_normal_paragraph(self):
        """Test with a standard multi-sentence paragraph."""
        text = "The quick brown fox jumps over the lazy dog. It was a sunny day. Are you ready?"
        stats = analyze_text(text)

        self.assertEqual(stats["total_characters"], len(text))
        self.assertEqual(stats["characters_no_spaces"], len(text.replace(" ", "")))
        self.assertEqual(stats["spaces"], text.count(" "))
        self.assertEqual(stats["words"], 17)
        self.assertEqual(stats["sentences"], 3)

        # Also verify individual functions
        total, without_spaces = count_characters(text)
        self.assertEqual(total, len(text))
        self.assertEqual(without_spaces, len(text.replace(" ", "")))
        self.assertEqual(count_words(text), 17)
        self.assertEqual(count_sentences(text), 3)
        self.assertEqual(count_spaces(text), text.count(" "))

    def test_empty_string(self):
        """Test with an empty string: all counts should be 0."""
        text = ""
        stats = analyze_text(text)

        self.assertEqual(stats["total_characters"], 0)
        self.assertEqual(stats["characters_no_spaces"], 0)
        self.assertEqual(stats["words"], 0)
        self.assertEqual(stats["sentences"], 0)
        self.assertEqual(stats["spaces"], 0)

        # Direct function calls
        total, without_spaces = count_characters(text)
        self.assertEqual(total, 0)
        self.assertEqual(without_spaces, 0)
        self.assertEqual(count_words(text), 0)
        self.assertEqual(count_sentences(text), 0)
        self.assertEqual(count_spaces(text), 0)

    def test_only_spaces(self):
        """Test with whitespace-only input: analyze_text should return 0 for all counts."""
        text = "      "
        stats = analyze_text(text)

        # Requirement 2: Handle empty input and whitespace-only input with all counts = 0
        self.assertEqual(stats["total_characters"], 0)
        self.assertEqual(stats["characters_no_spaces"], 0)
        self.assertEqual(stats["words"], 0)
        self.assertEqual(stats["sentences"], 0)
        self.assertEqual(stats["spaces"], 0)

        # Individual function behavior
        self.assertEqual(count_words(text), 0)
        self.assertEqual(count_sentences(text), 0)
        self.assertEqual(count_spaces(text), 6)
        total, without_spaces = count_characters(text)
        self.assertEqual(total, 6)
        self.assertEqual(without_spaces, 0)

    def test_multiple_spaces_between_words(self):
        """Test handling of irregular whitespace and multiple spaces between words."""
        text = "Hello    world!   This   is   a    test."
        stats = analyze_text(text)

        self.assertEqual(stats["words"], 6)
        self.assertEqual(stats["sentences"], 2)
        # Spaces: 4 + 3 + 3 + 3 + 4 = 17 spaces
        self.assertEqual(stats["spaces"], 17)
        self.assertEqual(stats["total_characters"], len(text))
        self.assertEqual(stats["characters_no_spaces"], len(text.replace(" ", "")))

    def test_consecutive_punctuation(self):
        """Test handling of consecutive punctuation like '...' and '?!'."""
        text = "Wait... really?! That is incredible!"
        stats = analyze_text(text)

        # 'Wait...' -> 1 ending
        # 'really?!' -> 1 ending
        # 'That is incredible!' -> 1 ending
        self.assertEqual(stats["sentences"], 3)
        self.assertEqual(stats["words"], 5)
        self.assertEqual(count_sentences(text), 3)

    def test_no_ending_punctuation(self):
        """Test text with no ending punctuation and trailing unpunctuated sentence."""
        # Single sentence with no terminal punctuation
        text_single = "This is a single sentence without any final punctuation"
        self.assertEqual(count_sentences(text_single), 1)

        # Multi-sentence where the last sentence lacks punctuation
        text_multi = "First sentence completed. Second sentence left hanging"
        self.assertEqual(count_sentences(text_multi), 2)
        stats = analyze_text(text_multi)
        self.assertEqual(stats["sentences"], 2)
        self.assertEqual(stats["words"], 7)

    def test_sample_paragraph_file(self):
        """Verify the built-in sample paragraph file matches calculated statistics."""
        sample_path = Path(__file__).parent / "sample_paragraph.txt"
        self.assertTrue(sample_path.exists(), "sample_paragraph.txt must exist")

        with open(sample_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

        stats = analyze_text(content)
        self.assertEqual(stats["total_characters"], 275)
        self.assertEqual(stats["characters_no_spaces"], 235)
        self.assertEqual(stats["words"], 41)
        self.assertEqual(stats["sentences"], 5)
        self.assertEqual(stats["spaces"], 40)

    def test_format_report(self):
        """Verify format_report outputs expected labels and values."""
        stats = {
            "total_characters": 100,
            "characters": 100,
            "characters_no_spaces": 80,
            "words": 15,
            "sentences": 2,
            "spaces": 20,
        }
        report = format_report(stats)
        self.assertIn("TEXT ANALYSIS REPORT", report)
        self.assertIn("100", report)
        self.assertIn("80", report)
        self.assertIn("15", report)
        self.assertIn("2", report)
        self.assertIn("20", report)


if __name__ == "__main__":
    unittest.main()
