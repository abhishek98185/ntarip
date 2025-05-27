from django.shortcuts import render, get_object_or_404
from .models import Paper, PaperName

# Create your views here.

def exam(request, year, name):
    number = int(name.split('-')[1]) if '-' in name else None
    # Get the PaperName object
    paper_name_obj = get_object_or_404(PaperName, name="JEE MAINS")
    # Get the Paper object for the given year and name
    paper = get_object_or_404(Paper, paper_name=paper_name_obj, year=year, number=number)

    mcq_questions = paper.mcq_questions.all()
    numerical_questions = paper.numerical_questions.all()

    context = {
        'paper': paper,
        'mcq_questions': mcq_questions,
        'numerical_questions': numerical_questions,
    }
    return render(request, 'jeemains.html', context)

