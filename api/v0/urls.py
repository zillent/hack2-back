from django.urls import path
from v0.views import  LogView

urlpatterns = [
    path('log/', LogView.as_view()),    
]
