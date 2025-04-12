from django.urls import path 
from . import views
from .views import weekly_schedule
from .views import weekly_schedule, delete_schedule

from .views import assistant_schedule
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.home, name="home"),
    path('notes/',views.notes, name="notes"),
    path('delete_note/<int:pk>/',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>/',views.NotesDetailView.as_view(),name="notes-detail"),


    path('homework',views.homework, name="homework"),
    path('update_homework/<int:pk>',views.update_homework, name="update-homework"),
    path('delete_homework/<int:pk>/',views.delete_homework,name="delete-homework"),


    path('youtube',views.youtube, name="youtube"),

    path('todo',views.todo, name="todo"),
    path('update_todo/<int:pk>',views.update_todo, name="update-todo"),
    path('delete_todo/<int:pk>/',views.delete_todo,name="delete-todo"),

    path('books',views.books, name="books"),

    path('dictionary',views.dictionary, name="dictionary"),

    path('wiki',views.wiki, name="wiki"),

    path('conversion',views.conversion, name="conversion"),  
 
    path('games/', views.games_view, name='games'),
    
    path('career/', views.career, name='career'),

    path('sem-temp/', views.sem_temp, name='sem_temp'),

    path('techstack/', views.techstack_view, name='techstack'),

    path('snapview/', views.snapview, name='snapview'),  

    path('pomodoro/', views.pomodoro_timer, name='pomodoro'),

    path('schedule/', weekly_schedule, name='schedule'),
    path('schedule/delete/<int:schedule_id>/', delete_schedule, name='delete_schedule'),

    path('assistant/schedule/', assistant_schedule, name='assistant-schedule'),
    path('assistant/', TemplateView.as_view(template_name="dashboard/assistant.html"), name="assistant"),
]


    






    
















