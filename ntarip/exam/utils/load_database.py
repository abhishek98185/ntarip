from exam.models import (physicsQuestionAndOptions, physicsQuestionAndNumerical,
                        chemistryQuestionAndOptions, chemistryQuestionAndNumerical,
                        mathsQuestionAndOptions, mathsQuestionAndNumerical, Paper, PaperName)
import json, datetime

def load_database():
    with open('ntarip/exam/static/json/jeemains28(2)jan2025_mcq.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open('ntarip/exam/static/json/jeemains28(2)jan2025_numerical.json', 'r', encoding='utf-8') as file:
        num_data = json.load(file)

    # Safer way to get the correct paper name
    paper_name = PaperName.objects.get(name__iexact="jee-mains")
    shift = 2
    # date = datetime.date(2025, 1, 22)  # Use real date instead of year + month + day
    year = 2025
    month = "January"
    day = 4
    paper = Paper.objects.create(
        paper_name=paper_name,
        year=year,
        month=month,
        day=day,
        shift=shift
    )

    for subject, question_dict in data.items():
        # physics = question_dict
        # options = question_dict.get("options", [])
        if subject.lower() == "physics":
            for question_data in question_dict:
                options = question_data.get("options", [])

                # Skip questions with invalid or missing options
                if not isinstance(options, list) or len(options) < 4:
                    continue

                physicsQuestionAndOptions.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    answer=question_data["answer"]
                )
        elif subject.lower() == "chemistry":
            for question_data in question_dict:
                options = question_data.get("options", [])

                # Skip questions with invalid or missing options
                if not isinstance(options, list) or len(options) < 4:
                    continue

                chemistryQuestionAndOptions.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    answer=question_data["answer"]
                )
        elif subject.lower() == "maths":
            for question_data in question_dict:
                options = question_data.get("options", [])

                # Skip questions with invalid or missing options
                if not isinstance(options, list) or len(options) < 4:
                    continue

                mathsQuestionAndOptions.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    answer=question_data["answer"]
                )

    for subject,question_dict in num_data.items():
        if subject.lower() == "physics":
            for question_data in question_dict:
                # Skip questions with invalid or missing options
                if not question_data.get("question") or not question_data.get("answer"):
                    continue
                physicsQuestionAndNumerical.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    answer=question_data["answer"]
                )
        elif subject.lower() == "chemistry":
            for question_data in question_dict:
                # Skip questions with invalid or missing options
                if not question_data.get("question") or not question_data.get("answer"):
                    continue
                chemistryQuestionAndNumerical.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    answer=question_data["answer"]
                )
        elif subject.lower() == "maths":
            for question_data in question_dict:
                # Skip questions with invalid or missing options
                if not question_data.get("question") or not question_data.get("answer"):
                    continue
                mathsQuestionAndNumerical.objects.create(
                    paper=paper,
                    question_text=question_data["question"],
                    answer=question_data["answer"]
                )
            
    print("Database loaded successfully.")

