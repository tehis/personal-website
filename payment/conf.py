import os
from personal import settings


API_KEY = '913b828a-be93-45c4-a83a-450c3049328a'
AMOUNT = 200
FREE_PDF_PATH = os.path.join(settings.BASE_DIR, 'payment', 'templates', '4-it.pdf')
NOT_FREE_PDF_PATH = os.path.join(settings.BASE_DIR, 'payment', 'templates', 'itil.pdf')
