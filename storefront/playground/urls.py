from django.urls import path
from . import views

#URLConfiguration for every app
urlpatterns = [
    path('hello/', views.say_hello)
    ##FOOOBBAAARRRR
]