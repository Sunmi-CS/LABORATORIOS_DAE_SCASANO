from django.urls import path
from . import views

urlpatterns = [
    # Vistas HTML
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', views.question_create, name='question_create'),

    # API JSON
    path('api/exams/', views.api_exams, name='api_exams'),                         # GET (lista), POST (crear)
    path('api/exams/<int:exam_id>/', views.api_exam_detail, name='api_exam_detail'),  # GET detalle anidado
    path('api/exams/<int:exam_id>/questions/', views.api_add_question, name='api_add_question'),  # POST pregunta




    # Endpoints API
    path('api/exams/', views.api_exams, name='api_exams'),
    path('api/exams/<int:exam_id>/', views.api_exam_detail, name='api_exam_detail'),



    path('frontend/', lambda r: render(r, "quiz/frontend.html")),

]
