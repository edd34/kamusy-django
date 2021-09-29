from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True)

    class Meta:
        ordering = ('name',)
  
    def __str__(self):
        return self.name
