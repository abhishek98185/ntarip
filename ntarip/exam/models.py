from django.db import models
from django.contrib.auth import get_user_model
class PaperName(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return f"{self.name}"
    
class Paper(models.Model):
    paper_name = models.ForeignKey(PaperName, on_delete=models.CASCADE, related_name='papers')
    year = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.paper_name} ({self.year}) - {self.number}"
class QuestionAndOptions(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
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
    question = models.ForeignKey(QuestionAndOptions, on_delete=models.CASCADE)
    answersheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    start_time = models.TimeField(null=True, blank=True)
    def __str__(self):
        return f"Answer for {self.question.question_text} by {self.answersheet.user.username} - {'Correct' if self.is_correct else 'Incorrect'}"
