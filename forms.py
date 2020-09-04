from school_track.models import Subject, Assignment
from django import forms

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['text']
        labels = {'text': ''}

ass_years = ('2020', '2021', '2022', '2023', '2024')

assignment_types = (
    ('TEST', 'Test'),
    ('QUIZ', 'Quiz'),
    ('PROJECT', 'Project'),
    ('CLASSWORK', 'Classwork'),
    ('HOMEWORK', 'Homework')
)

class AssignmentForm(forms.ModelForm):

    
    class Meta:
        model = Assignment
        fields = ['assignment', 'due_date']
        widgets = {
            'assignment': forms.Textarea(), 
            'due_date': forms.SelectDateWidget(years=ass_years)
        }