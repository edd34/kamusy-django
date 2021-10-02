from django.db import models
from components.language.models import Language


class Word(models.Model):
    name = models.CharField(max_length=150)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # alpha_position = models.CharField(max_length=2, db_index=True, editable=True, blank=False, null=False, choices=ALPHABET_CHOICES, verbose_name=_('Alphabet Position'), help_text=_('Show this entry under which Alphabet position'))
    # description = models.TextField(blank=False, verbose_name=_('The Explanation'), help_text=_('The description of the term being explained'))
    # translation

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
