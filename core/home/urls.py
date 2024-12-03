from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    # path('',home),
    # path('student/',student_post),
    # path('update-student/<id>/',update_student),
    # path('delete-student/<id>/',delete_student),
    path('student/',StudentApi.as_view()),
    path('student/<int:pk>/',StudentApi.as_view()),
    path('books/',get_books),
    path('register/',RegisterUser.as_view())
]