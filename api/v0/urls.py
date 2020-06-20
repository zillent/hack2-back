from django.urls import path
from v0.views import  (
    LogView,
    OfferView, SingleOfferView
)

urlpatterns = [
    path('log/', LogView.as_view()),    
    path('offer/', OfferView.as_view()),    
    path('offer/<int:pk>', SingleOfferView.as_view()),    
]
