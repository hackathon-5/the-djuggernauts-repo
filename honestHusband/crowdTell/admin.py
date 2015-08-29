from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    pass


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


class PictureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Picture, PictureAdmin)