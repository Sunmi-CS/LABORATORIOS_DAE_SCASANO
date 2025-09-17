from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet

# ---------- VISTAS HTML ----------
def exam_list(request):
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Examen creado correctamente.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()
    return render(request, 'quiz/exam_form.html', {'form': form})

def question_create(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            with transaction.atomic():
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()

                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()
                    correct_count = question.choices.filter(is_correct=True).count()
                    if correct_count != 1:
                        messages.warning(request, 'Debe haber exactamente una respuesta correcta.')
                    else:
                        messages.success(request, 'Pregunta añadida correctamente.')

                    if 'add_another' in request.POST:
                        return redirect('question_create', exam_id=exam.id)
                    else:
                        return redirect('exam_detail', exam_id=exam.id)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()

    return render(request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })

# ---------- API JSON (endpoints) ----------
# Nota: @csrf_exempt SOLO para laboratorio/desarrollo.
# En producción, usa tokens CSRF o auth.
@csrf_exempt
def api_exams(request):
    if request.method == 'GET':
        data = [
            {
                'id': e.id,
                'title': e.title,
                'description': e.description,
                'created_date': e.created_date.isoformat(),
                'question_count': e.get_question_count(),
            }
            for e in Exam.objects.all().order_by('-created_date')
        ]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload.get('title', '').strip()
            description = payload.get('description', '').strip()
            if not title:
                return HttpResponseBadRequest('title es requerido')
            exam = Exam.objects.create(title=title, description=description)
            return JsonResponse({'id': exam.id, 'title': exam.title, 'description': exam.description}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))

    return HttpResponseBadRequest('Método no permitido')

def api_exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    data = {
        'id': exam.id,
        'title': exam.title,
        'description': exam.description,
        'created_date': exam.created_date.isoformat(),
        'questions': [
            {
                'id': q.id,
                'text': q.text,
                'choices': [
                    {'id': c.id, 'text': c.text, 'is_correct': c.is_correct}
                    for c in q.choices.all()
                ],
            }
            for q in exam.questions.all().prefetch_related('choices')
        ],
    }
    return JsonResponse(data)

@csrf_exempt
def api_add_question(request, exam_id):
    if request.method != 'POST':
        return HttpResponseBadRequest('Método no permitido')

    exam = get_object_or_404(Exam, id=exam_id)
    try:
        payload = json.loads(request.body.decode('utf-8'))
        text = payload.get('text', '').strip()
        choices = payload.get('choices', [])

        if not text:
            return HttpResponseBadRequest('text es requerido')
        if not isinstance(choices, list) or len(choices) < 2:
            return HttpResponseBadRequest('Se requieren al menos 2 choices')

        correct_count = sum(1 for ch in choices if ch.get('is_correct') is True)
        if correct_count != 1:
            return HttpResponseBadRequest('Debe haber exactamente 1 choice is_correct=true')

        with transaction.atomic():
            q = Question.objects.create(exam=exam, text=text)
            for ch in choices:
                Choice.objects.create(
                    question=q,
                    text=ch.get('text', '').strip(),
                    is_correct=bool(ch.get('is_correct', False))
                )

        return JsonResponse({'question_id': q.id}, status=201)

    except Exception as e:
        return HttpResponseBadRequest(str(e))















from django.http import JsonResponse

# Endpoint para devolver todos los exámenes
def api_exams(request):
    exams = list(Exam.objects.values("id", "title", "description", "created_date"))
    return JsonResponse(exams, safe=False)

# Endpoint para devolver las preguntas de un examen
def api_exam_detail(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    questions = exam.questions.all().prefetch_related("choices")

    data = {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "questions": []
    }

    for question in questions:
        data["questions"].append({
            "id": question.id,
            "text": question.text,
            "choices": [
                {"id": c.id, "text": c.text, "is_correct": c.is_correct}
                for c in question.choices.all()
            ]
        })

    return JsonResponse(data, safe=False)
