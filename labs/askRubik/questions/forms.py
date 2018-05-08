from django import forms

from .models import Question




class QuestionForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False, label='Tags (comma separated)')

    class Meta:
        model = Question
        fields = ['title', 'text']
