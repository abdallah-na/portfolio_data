from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/',views.AboutMe,name='about me'),

    path('projects/',views.project,name='all projects'),
    path('project/<slug:slug>',views.project_detail,name='project details'),

    path('works/',views.work,name='all work'),
    path('work/<slug:slug>',views.work_detail,name='work details'),

    path('Educations/',views.Education,name='all education history'),
    path('Education/<slug:slug>',views.Education_detail,name='education history details'),
]
