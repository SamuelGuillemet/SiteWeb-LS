from django.contrib import admin
from .models import Article, Source, Theme


class ThemeInLine(admin.StackedInline):
    model = Theme
    extra = 0


class SourceInLine(admin.TabularInline):
    model = Source
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['publication']
    inlines = [ThemeInLine, SourceInLine]
    list_display = ('title', 'publication',
                    'published_date', 'was_published_recently')


# Register your models here.
admin.site.register(Article, ArticleAdmin)
