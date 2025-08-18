from django.db import models
from django.conf import settings

class Test(models.Model):
    title = models.CharField(max_length=200)
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    is_access = models.BooleanField(default=True)
    def __str__(self): return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    def __str__(self): return self.text[:50]

class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="variants")
    text = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)
    def __str__(self): return f"{self.text} ({'Correct' if self.is_true else 'Wrong'})"

class Answer(models.Model):
    # IMPORTANT: refer to custom user model
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.student.username} - {self.variant.text}"
