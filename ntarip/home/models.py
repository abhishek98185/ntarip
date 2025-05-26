from django.db import models

# Create your models here.
class Paper(models.Model):
    paper_name = models.CharField(max_length=255)
    paper_date = models.DateField()
class QuestionAndOptions(models.Model):
    question_text = models.CharField(max_length=255)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='questions')
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
class UserAnswer(models.Model):
    user = models.CharField(max_length=255)
    question = models.ForeignKey(QuestionAndOptions, on_delete=models.CASCADE, related_name='user_answers')
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'question')

