from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),

    path("<int:question_id>/", views.detail, name="detail"),

    path("<int:question_id>/resultados/", views.results, name="resultados"),

    path("<int:question_id>/votar/", views.vote, name="votar")
]

