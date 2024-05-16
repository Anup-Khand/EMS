from student import views
from django.urls import path
urlpatterns = [
    
     path('student/', views.student_api),
]