from django.shortcuts import render # type: ignore
from .models import Quiz
from .forms import QuizForm
from django.shortcuts import get_object_or_404,redirect # type: ignore

# Create your views here.

def index(request):
    return render(request, 'index.html')

def quiz_list(request):
    quizes = Quiz.objects.all().order_by('-created_at')
    return render(request,'quiz_list.html',{'quizes':quizes})

def quiz_create(request):
    if request.method == "POST":
        form = QuizForm(request.POST,request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request,'quiz_form.html', {'form':form})

def quiz_edit(request,quiz_id):
    quiz = get_object_or_404(Quiz,pk = quiz_id, user = request.user)
    if request.method == 'POST':
        form = QuizForm(request.POST,request.FILES,instance=quiz)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'quiz_form.html', {'form':form})

def quiz_delete(request,quiz_id):
    quiz = get_object_or_404(Quiz,pk = quiz_id, user = request.user)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')
    return render(request,'quiz_confirm_delete.html',{'quiz':quiz})