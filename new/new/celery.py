from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new.settings')

app = Celery('new')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_news_from_ria_ru': {
        'task': 'newpols.tasks.get_news_from_ria_ru',
        'schedule': crontab(minute='*/1'),
    },
}
app.conf.timezone = 'Asia/Bishkek'

def debug_task(self):
	print('Request: {0!r}').format(self.request)
