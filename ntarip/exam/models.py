from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class PaperName(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return f"{self.name}"
    
class Paper(models.Model):
    paper_name = models.ForeignKey(PaperName, on_delete=models.CASCADE, related_name='papers')
    shift = models.IntegerField(null=True, blank=True)
    # date = models.DateField(null=True, blank=True)
    

    year = models.PositiveIntegerField(null=True, blank=True)
    # Using PositiveSmallIntegerField for month to limit values to 1-12
    day = models.PositiveSmallIntegerField(null=True, blank=True)
    month = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.paper_name} ({self.year}-{self.month})-day-{self.day}- Shift {self.shift}"

class physicsQuestionAndOptions(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='physics_mcq_questions')
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"
class physicsQuestionAndNumerical(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='physics_numerical_questions')
    question_text = models.CharField(max_length=255)
    
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"


class chemistryQuestionAndOptions(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='chemistry_mcq_questions')
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"
class chemistryQuestionAndNumerical(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='chemistry_numerical_questions')
    question_text = models.CharField(max_length=255)
    
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"


class mathsQuestionAndOptions(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='maths_mcq_questions')
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"
class mathsQuestionAndNumerical(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='maths_numerical_questions')
    question_text = models.CharField(max_length=255)
    
    answer = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.question_text} - {self.paper.paper_name.name}"



class AnswerSheet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"AnswerSheet for {self.user.username} - {self.paper.paper_name.name} ({self.submitted_at})"

class UserAnswer(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    question = GenericForeignKey('content_type', 'object_id')
    
    answersheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    start_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Answer for {self.question} by {self.answersheet.user.username} - {'Correct' if self.is_correct else 'Incorrect'}"