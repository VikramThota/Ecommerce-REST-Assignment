from django.urls import path
from .views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('<str:pk>', ProductsView.as_view())
]
