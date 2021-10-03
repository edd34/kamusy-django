from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.management.base import BaseCommand
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
        print(df)
        print(Language, Word, Translation)
        