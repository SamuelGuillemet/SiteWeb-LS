from django.contrib import admin
from .models import CV, Experience, Project, Skill, Social
# Register your models here.


class SkillsInLine(admin.TabularInline):
    model = Skill
    extra = 2


class ProjetcsInLine(admin.TabularInline):
    model = Project
    extra = 3


class ExperiencesInLine(admin.TabularInline):
    model = Experience
    extra = 3


class SocialInLine(admin.TabularInline):
    model = Social
    extra = 2


class CVAdmin(admin.ModelAdmin):
    inlines = [SkillsInLine, ProjetcsInLine, ExperiencesInLine, SocialInLine]


admin.site.register(CV, CVAdmin)
