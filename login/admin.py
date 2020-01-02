from django.contrib import admin
from .models import match_list,game_list
# Register your models here.
admin.site.register(match_list)
admin.site.register(game_list)