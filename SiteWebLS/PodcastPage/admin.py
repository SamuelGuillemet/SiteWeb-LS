from django.contrib import admin
from .models import Podcast, Theme, Chapitre

# Register your models here.


class ThemeInLine(admin.StackedInline):
    model = Theme
    extra = 0


class ChapitreInLine(admin.TabularInline):
    model = Chapitre
    extra = 4


class PodcastAdmin(admin.ModelAdmin):
    inlines = [ThemeInLine, ChapitreInLine]


admin.site.register(Podcast, PodcastAdmin)
