from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Questions
        fields = ['question_text', 'pub_date']


class PesertaForm(forms.Form):
    nama = forms.CharField()
    asal = forms.CharField()


class TambahForm(forms.Form):
    angka1 = forms.IntegerField()
    angka2 = forms.IntegerField()