from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    # These are the subjects which the user will input:
    text = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text

assignment_types = (
    ('TEST', 'Test'),
    ('QUIZ', 'Quiz'),
    ('PROJECT', 'Project'),
    ('CLASSWORK', 'Classwork'),
    ('HOMEWORK', 'Homework')
)

class Assignment(models.Model):
    subjects = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    assignment = models.TextField(max_length=100)
    due_date = models.DateField(null=True)
    

    class Meta:
        verbose_name_plural = 'assignments'

    def __str__(self):
        return self.assignment

