from django.core.management.base import BaseCommand
from django.core.management import call_command
from components.word.models import Word
from components.translation.models import Translation
from components.language.models import Language

import pandas as pd
import numpy as np

from utils.parse_dict import main

class Command(BaseCommand):
    help = 'import database'

    def handle(self, *args, **kwargs):
        df = main()

        mahorais = Language.objects.get_or_create(name="mahorais")
        francais = Language.objects.get_or_create(name="français")

        res = Language.objects.all()
        print(res.values_list('pk', flat=True))

        def create_translation(row):
            word_mahorais = Word.objects.get_or_create(name=row["mahorais"], language=mahorais[0])
            word_francais = Word.objects.get_or_create(name=row["français"], language=francais[0])
            Translation.objects.get_or_create(word_source=word_mahorais[0], language_source=mahorais[0], word_destination=word_francais[0], language_destination=francais[0])
            Translation.objects.get_or_create(word_source=word_francais[0], language_source=francais[0], word_destination=word_mahorais[0], language_destination=mahorais[0])

        df.apply(lambda x: create_translation(x), axis=1)
