from django.db import models

from components.language.models import Language
from components.word.models import Word


class Translation(models.Model):
    word_source = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name="w_source"
    )
    language_source = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="l_source"
    )
    word_destination = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name="w_destination"
    )
    language_destination = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="l_destination"
    )
