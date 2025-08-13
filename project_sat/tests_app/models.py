from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


# Test / Quiz
class Test(models.Model):
    title = models.CharField(max_length=200)
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    is_access = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Question inside a Test
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


# Variants for each Question
class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="variants")
    text = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_true else 'Wrong'})"


# Answers by Students
class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.variant.text}"
