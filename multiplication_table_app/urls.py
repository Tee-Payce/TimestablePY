from django.urls import path
from . import views

app_name = 'multiplication_table_app'

urlpatterns = [
    path('table/', views.multiplication_table_view, name='multiplication_table'),
]
