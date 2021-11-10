r"""The module for regex characters like :code:`\w` or :code:`\D` or :code:`.`"""

from .pattern import RegexPattern, escape


class RegexChar(RegexPattern):
    """The base class that deals with escaped and special regex characters."""
    regex: str = ''

    def __init__(self, character: str = None):
        if character:
            self.regex = escape(character)


class Whitespace(RegexChar):
    """
    Matches any whitespace character.
    A whitespace character is one of these characters.
    :code:`"\\n"`, :code:`"\\r"`, :code:`"\\v"`, :code:`"\\f"`, :code:`"\\t"`, :code:`" "`.
    """

    regex = r'\s'


class NotWhitespace(RegexChar):
    """Matches any character that is not a whitespace character."""

    regex = r'\S'


class Any(RegexChar):
    """Matches any character except the newline character."""

    regex = r'.'


class Word(RegexChar):
    """1234567890"""

    regex = r'\w'


class NotWord(RegexChar):
    """1234567890"""

    regex = r'\W'


class Digit(RegexChar):
    """1234567890"""

    regex = r'\d'


class NotDigit(RegexChar):
    """1234567890"""

    regex = r'\D'


ANY = Any()
"""1234567890"""


WHITESPACE = Whitespace()
"""1234567890"""


NOTWHITESPACE = NotWhitespace()
"""1234567890"""


WORD = Word()
"""1234567890"""


NOTWORD = NotWord()
"""1234567890"""


DIGIT = Digit()
"""1234567890"""


NOTDIGIT = NotDigit()
"""1234567890"""

