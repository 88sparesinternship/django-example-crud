from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index_question, name='index'),
    path('create', views.create_question, name='create'),
    path('update/<int:question_id>/', views.update_question, name='update'),
    path('delete/<int:question_id>/', views.delete_question, name='hapus')
]