from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('', views.student_api),
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),

]
