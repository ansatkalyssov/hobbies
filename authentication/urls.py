from authentication import views
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('', views.Login.as_view(), name='login')
]
