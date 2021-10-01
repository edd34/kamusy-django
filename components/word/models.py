from django.db import models
from components.language.models import Language


class Word(models.Model):
    name = models.CharField(max_length=150)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
