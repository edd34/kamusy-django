from django.core.management.base import BaseCommand
from django.core.management import call_command
from components.word.models import Word
from components.translation.models import Translation
from components.language.models import Language

import pandas as pd
import numpy as np

from utils.parse_dict import get_dict_kibushi, get_dict_mahorais

class Command(BaseCommand):
    help = 'import database'

    def handle(self, *args, **kwargs):
        df = get_dict_mahorais()
        df1 = get_dict_kibushi()

        mahorais = Language.objects.get_or_create(name="mahorais")
        francais = Language.objects.get_or_create(name="français")
        kibushi = Language.objects.get_or_create(name="kibushi")

        res = Language.objects.all()
        print(res.values_list('pk', flat=True))

        def create_translation_mahorais_fr(row):
            word_mahorais = Word.objects.get_or_create(name=row["mahorais"], language=mahorais[0])
            word_francais = Word.objects.get_or_create(name=row["français"], language=francais[0])
            Translation.objects.get_or_create(word_source=word_mahorais[0], language_source=mahorais[0], word_destination=word_francais[0], language_destination=francais[0])
            Translation.objects.get_or_create(word_source=word_francais[0], language_source=francais[0], word_destination=word_mahorais[0], language_destination=mahorais[0])

        def create_translation_kibushi_fr(row):
            word_kibushi = Word.objects.get_or_create(name=row["kibushi"], language=kibushi[0])
            word_francais = Word.objects.get_or_create(name=row["français"], language=francais[0])
            Translation.objects.get_or_create(word_source=word_kibushi[0], language_source=kibushi[0], word_destination=word_francais[0], language_destination=francais[0])
            Translation.objects.get_or_create(word_source=word_francais[0], language_source=francais[0], word_destination=word_kibushi[0], language_destination=kibushi[0])

        df.apply(lambda x: create_translation_mahorais_fr(x), axis=1)
        df1.apply(lambda x: create_translation_kibushi_fr(x), axis=1)
