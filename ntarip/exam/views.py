from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Paper, PaperName, AnswerSheet, UserAnswer
from django.utils.dateparse import parse_time
import json

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
            'Physics' : physics_questions,
            'Chemistry' : chemistry_questions,
            'Maths' : maths_questions,
            'exam': exam,
            'examData':{'exam':exam,'year':year,'month':month,'day':day}
        }

        return render(request, 'jeemains.html', context)
    # return render(request, 'jeemains.html')
@csrf_exempt
def submit_answers(request):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=403)

        data = json.loads(request.body)
        paper_id = data.get("paper_id")
        answers = data.get("answers", [])

        try:
            paper = Paper.objects.get(paper_id=paper_id)
        except Paper.DoesNotExist:
            return JsonResponse({'error': 'Paper not found'}, status=404)

        answersheet = AnswerSheet.objects.create(user=user, paper=paper)

        for ans in answers:
            question_type = ans.get("question_type")  # e.g., "mcq", "written"
            question_id = ans.get("question_id")
            answer_text = ans.get("answer")
            is_correct = ans.get("is_correct", False)
            start_time = parse_time(ans.get("start_time"))

            try:
                content_type = ContentType.objects.get(model=question_type)
            except ContentType.DoesNotExist:
                continue  # or return error

            UserAnswer.objects.create(
                content_type=content_type,
                object_id=question_id,
                answersheet=answersheet,
                answer=answer_text,
                is_correct=is_correct,
                start_time=start_time
            )

        return JsonResponse({'message': 'Answers submitted successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)