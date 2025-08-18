# tests/models.py
from django.db import models
from accounts.models import User

class Test(models.Model):
    title = models.CharField(max_length=255)
    time_limit = models.PositiveIntegerField(help_text="Time in minutes")
    is_access = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="variants")
    text = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_variant = models.ForeignKey(Variant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} → {self.chosen_variant.text}"
