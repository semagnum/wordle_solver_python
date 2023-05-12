from enum import IntEnum

FREQUENCY = list('eariotnslcudpmhgbfywkvxzjq')
"""Letters sorted in most popular letters. Helps sort potential words by the most popular letters.
By using and potentially eliminating popular letters, more words can be filtered."""

WORD_SIZE = 5
"""Word size for Wordle puzzle."""


class Correctness(IntEnum):
    """Shows the three possible outcomes for a letter choice:
    correct (green),
    correct letter but wrong position (yellow),
    and incorrect letter and position (grey)."""
    CORRECT = 1
    WRONG_POSITION = 2
    WRONG_LETTER = 3


