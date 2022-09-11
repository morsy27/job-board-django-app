from django.urls import path , include
from . import views

app_name = 'job'

urlpatterns = [
    path('',views.job_list, name='jobs'),
    path('<int:id>',views.job_details,name='job_details'),
]