import csv
import datetime

import numpy as np
import pandas as pd
from django.core.management import call_command
from django.core.management.base import BaseCommand

from components.language.models import Language
from components.language.serializers import LanguageSerializer
from components.translation.models import Translation
from components.translation.serializers import GetTranslationSerializer
from components.word.models import Word
from components.word.serializers import WordSerializer
from utils.parse_dict import get_dict_kibushi, get_dict_mahorais


class Command(BaseCommand):
    help = "export database"

    def handle(self, *args, **kwargs):

        filename = (
            str(datetime.datetime.now().timestamp()).replace(".", "_")
            + "_export_db.csv"
        )

        translation = Translation.objects.all()
        translation_s = GetTranslationSerializer(translation, many=True)

        df = pd.DataFrame(translation_s.data)
        df.to_csv(filename)
