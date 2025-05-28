from django.shortcuts import render, get_object_or_404
from .models import Paper, PaperName
import datetime

# Create your views here.

def exam(request):
    exam = request.GET.get('exam')  # jee-mains
    year = request.GET.get('year')  # 2015
    month = request.GET.get('month')  # January
    day = request.GET.get('day')  # 1

    shift = request.GET.get('shift')  # 1
    if exam is None or year is None or month is None or day is None or shift is None:
        return render(request, 'error.html', {'message': 'Invalid parameters'})
    # date = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%B-%d")
    if exam == "jee-mains":
        # Get the PaperName object
        paper_name_obj = get_object_or_404(PaperName, name="jee-mains")
        # Get the Paper object for the given year and name
        paper = get_object_or_404(Paper, paper_name=paper_name_obj, shift=shift,year=year, month=month, day=day)

        
        physics_questions = list(paper.physics_mcq_questions.all()) + list(paper.physics_numerical_questions.all())
        chemistry_questions = list(paper.chemistry_mcq_questions.all()) + list(paper.chemistry_numerical_questions.all())
        maths_questions = list(paper.maths_mcq_questions.all()) + list(paper.maths_numerical_questions.all())

        Questions = physics_questions + chemistry_questions + maths_questions

        context = {
            'paper': paper,
            'Questions': Questions,
            'exam': exam,
        }

        return render(request, 'jeemains.html', context)
    # return render(request, 'jeemains.html')

