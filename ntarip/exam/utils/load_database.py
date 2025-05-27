from exam.models import QuestionAndOptions, QuestionAndNumerical, Paper, PaperName
import json

def load_database():
    with open('ntarip/exam/jeemains_mcq.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open('ntarip/exam/jeemains_numerical.json', 'r', encoding='utf-8') as file:
        num_data = json.load(file)

    # Safer way to get the correct paper name
    paper_name = PaperName.objects.get(name__iexact="JEE MAINS")
    year = 2025
    number = 1

    paper, created = Paper.objects.get_or_create(
        paper_name=paper_name,
        year=year,
        number=number
    )

    for subject, question_dict in data.items():
        # physics = question_dict
        # options = question_dict.get("options", [])
        for question_data in question_dict:
            options = question_data.get("options", [])

            # Skip questions with invalid or missing options
            if not isinstance(options, list) or len(options) < 4:
                continue

            QuestionAndOptions.objects.create(
                paper=paper,
                question_text=question_data["question"],
                option1=options[0],
                option2=options[1],
                option3=options[2],
                option4=options[3],
                answer=question_data["answer"]
            )

    for subject,question_dict in num_data.items():
        for question_data in question_dict:
            # Skip questions with invalid or missing options
            if not question_data.get("question") or not question_data.get("answer"):
                continue
            QuestionAndNumerical.objects.create(
                paper=paper,
                question_text=question_data["question"],
                answer=question_data["answer"]
            )
    print("Database loaded successfully.")

