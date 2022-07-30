from django.db import models
from components.language.models import Language


def getAlphabet(begin="a", end="z"):
    """
    Return a list of Alphabet entries in a configurable range

    Valid Useage
    >>> a = getAlphabet('a', 'c')
    >>> print a
    [('a', 'a'), ('b', 'b'), ('c', 'c')]

    Invalid Useage
    >>> a = getAlphabet('z', 'c')
    >>> print a
    []
    """
    dictionary = []
    beginNum = ord(begin)
    endNum = ord(end)
    for number in range(beginNum, endNum + 1):
        character = chr(number)
        dictionary.append((character, character))
    return dictionary


# Alphabet Constant for re-use in context and views
ALPHABET_CHOICES = getAlphabet()


class Word(models.Model):
    name = models.CharField(max_length=150)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    alpha_position = models.CharField(
        max_length=2,
        db_index=True,
        editable=True,
        blank=False,
        null=False,
        choices=ALPHABET_CHOICES,
        verbose_name=("Alphabet Position"),
        help_text=("Show this entry under which Alphabet position"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=("The Explanation"),
        help_text=("The description of the term being explained"),
        null=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
