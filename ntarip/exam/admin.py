from django.contrib import admin

# Register your models here.
from .models import Paper, PaperName, QuestionAndOptions, QuestionAndNumerical, AnswerSheet, UserAnswer

admin.site.register(PaperName)
admin.site.register(Paper)
admin.site.register(QuestionAndOptions)
admin.site.register(QuestionAndNumerical)
admin.site.register(AnswerSheet)
admin.site.register(UserAnswer)