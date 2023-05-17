from django.urls import path
from . import views

urlpatterns = [
    path('add_conta/', views.add_conta, name="add_conta"),
    path('conta/<slug:slug>', views.Conta, name="conta")
]
