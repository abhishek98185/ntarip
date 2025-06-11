from django.contrib import admin

# Register your models here.
from .models import (Paper, PaperName, physicsQuestionAndOptions, physicsQuestionAndNumerical, 
                     chemistryQuestionAndOptions, chemistryQuestionAndNumerical, 
                     mathsQuestionAndOptions, mathsQuestionAndNumerical, AnswerSheet, UserAnswer)
from django.contrib import admin
from .models import chemistryQuestionAndOptions

class Search(admin.ModelAdmin):
    search_fields = [
        'question_text',
        'paper__paper_name__name',  # assuming paper_name is a FK in Paper
        'paper__year',
        'paper__month',
        'paper__day',
        'paper__shift',
        
    ]
    
    list_filter = ['paper__year', 'paper__month', 'paper__shift']  # Add filter dropdowns in sidebar
    list_display = ['paper__day','question_text', 'paper', 'is_image']  # Optional: show key info in list view


admin.site.register(PaperName)
admin.site.register(Paper)
admin.site.register(physicsQuestionAndOptions,Search)
admin.site.register(physicsQuestionAndNumerical,Search)
admin.site.register(chemistryQuestionAndOptions,Search)
admin.site.register(chemistryQuestionAndNumerical,Search)
admin.site.register(mathsQuestionAndOptions,Search)
admin.site.register(mathsQuestionAndNumerical,Search)
admin.site.register(AnswerSheet)
admin.site.register(UserAnswer)