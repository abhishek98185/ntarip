from django.contrib import admin

# Register your models here.
from .models import (Paper, PaperName, physicsQuestionAndOptions, physicsQuestionAndNumerical, 
                     chemistryQuestionAndOptions, chemistryQuestionAndNumerical, 
                     mathsQuestionAndOptions, mathsQuestionAndNumerical, AnswerSheet, UserAnswer)

admin.site.register(PaperName)
admin.site.register(Paper)
admin.site.register(physicsQuestionAndOptions)
admin.site.register(physicsQuestionAndNumerical)
admin.site.register(chemistryQuestionAndOptions)
admin.site.register(chemistryQuestionAndNumerical)
admin.site.register(mathsQuestionAndOptions)
admin.site.register(mathsQuestionAndNumerical)
admin.site.register(AnswerSheet)
admin.site.register(UserAnswer)