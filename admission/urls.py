from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddStudent.as_view(), name="Add Student"),
    path(r'', views.AddStudent.as_view()),
]