from django.core.management.base import BaseCommand
from django.core.management import call_command
from components.word.models import Word
from components.translation.models import Translation
from components.language.models import Language
from components.word.serializers import WordSerializer
from components.translation.serializers import GetTranslationSerializer
from components.language.serializers import LanguageSerializer

import pandas as pd
import numpy as np
import csv
import datetime

from utils.parse_dict import get_dict_kibushi, get_dict_mahorais


class Command(BaseCommand):
    help = 'export database'

    def handle(self, *args, **kwargs):

        filename = str(datetime.datetime.now().timestamp()
                       ).replace(".", "_") + "_export_db.csv"

        translation = Translation.objects.all()
        translation_s = GetTranslationSerializer(translation, many=True)

        df = pd.DataFrame(translation_s.data)
        df.to_csv(filename)
