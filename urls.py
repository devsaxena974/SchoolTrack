from school_track import views
from django.urls import path

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'subjects/(?<subject_id>\d+)/', views.subjects, name='subjects'),
    path(r'new_subject/', views.new_subject, name='new_subject'),
    path(r'^new_assignment/(?<subject_id>\d+)/', views.new_assignment, name='new_assignment'),
    path(r'^edit_assignment/(?<assignment_id>\d+)/', views.edit_assignment, name='edit_assignment'),
    path(r'^delete_assignment/(?<assignment_id>\d+)/', views.delete_assignment, name='delete_assignment')
]