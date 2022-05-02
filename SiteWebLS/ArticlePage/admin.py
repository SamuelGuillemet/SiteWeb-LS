from django.contrib import admin
from .models import Article, Theme


class ThemeInLine(admin.StackedInline):
    model = Theme
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['publication']
    inlines = [ThemeInLine]
    list_display = ('title', 'publication',
                    'published_date', 'was_published_recently')


# Register your models here.
admin.site.register(Article, ArticleAdmin)
