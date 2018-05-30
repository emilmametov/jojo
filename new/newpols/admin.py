from django.contrib import admin
from .models import News
from sports.models import Sport
from politics.models import Politics
admin.site.register(News)
admin.site.register(Sport)
admin.site.register(Politics)