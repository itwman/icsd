from django.urls import path

from . import views

app_name = "academy"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("certificate/<uuid:code>/", views.certificate_view, name="certificate"),
    path("<slug:slug>/", views.course_detail, name="course_detail"),
    path("<slug:slug>/enroll/", views.enroll, name="enroll"),
    path("<slug:slug>/learn/", views.learn_start, name="learn_start"),
    path("<slug:slug>/learn/<int:lesson_id>/", views.learn, name="learn"),
    path("<slug:slug>/learn/<int:lesson_id>/done/", views.complete_lesson, name="complete"),
    path("<slug:slug>/quiz/", views.quiz_start, name="quiz_start"),
    path("<slug:slug>/quiz/begin/", views.quiz_begin, name="quiz_begin"),
    path("<slug:slug>/quiz/<int:attempt_id>/", views.quiz_take, name="quiz_take"),
    path("<slug:slug>/quiz/<int:attempt_id>/result/", views.quiz_result, name="quiz_result"),
]
