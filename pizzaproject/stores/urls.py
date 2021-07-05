from django.urls import path
from . import views

# store
urlpatterns = [
    path('', views.PizzeriaListAPIView.as_view(), name="pizzeria_list"),
]

