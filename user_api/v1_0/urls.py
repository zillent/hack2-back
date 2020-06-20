from django.urls import path
from v1_0.views import  (
    LogView,
    PersonView, SinglePersonView
)

urlpatterns = [
    path('log/', LogView.as_view()),    
    path('person/', PersonView.as_view()),    
    path('person/<int:pk>', SinglePersonView.as_view()),    
]
