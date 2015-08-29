from django.contrib import admin

from .models import *


class PersonAdmin(admin.ModelAdmin):
    pass


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 1


class PictureQuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


admin.site.register(Person, PersonAdmin)
admin.site.register(PictureQuestion, PictureQuestionAdmin)