from django.contrib import admin
from assignmentapp.models import Types_Of_Games
# Register your models here.

class Types_Of_GamesAdmin(admin.ModelAdmin):
    list_display = ('name','releasedate','type')

admin.site.register(Types_Of_Games, Types_Of_GamesAdmin)