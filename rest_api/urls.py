from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/', views.student_detail),
    #path('student_info/', views.student_list),
    path('student_create/', views.student_create),
    path('student_update/', views.student_update),
    path('student_delete/', views.student_delete),
    path('hello/', views.hello),
]
