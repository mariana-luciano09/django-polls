from django.urls import path
from . import views

urlpatterns = [

    # path("", views.index, name="index"),

    # path("<int:question_id>/", views.detail, name="detail"),

    # path("<int:question_id>/resultados/", views.results, name="results"),

    # path("<int:question_id>/votar/", views.vote, name="vote"),

    path('listar', views.QuestionListView.as_view(), name='question-list'),

    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),

    path('<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),

    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete')
]