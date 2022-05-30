from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_text', 'votes']


admin.site.register(Question)
admin.site.register(Choice)
