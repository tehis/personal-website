import os
from personal import settings


API_KEY = '913b828a-be93-45c4-a83a-450c3049328a'
AMOUNT = 1000
FREE_PDF_PATH = os.path.join(settings.BASE_DIR, 'payment', 'templates', 'about course.pdf')
NOT_FREE_PDF_PATH = os.path.join(settings.BASE_DIR, 'payment', 'templates', 'summary.pdf')
