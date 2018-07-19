from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuestionForm
from .models import Questions


def index_question(request):
    context = {
        'questions': Questions.objects.all()
    }
    return render(request, 'polls/index.html', context)


def create_question(request):
    form = QuestionForm(request.POST or None, use_required_attribute=False)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('polls:index')

    context = {
        'form': form,
        'update': False,
    }
    return render(request, 'polls/form.html', context)


def update_question(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('polls:index')

    context = {
        'form': form,
        'update': True,
    }
    return render(request, 'polls/form.html', context)


def delete_question(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    question.delete()
    return redirect('polls:index')
