from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubCategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register("", SubCategoryViewSet, basename='sub_category')

urlpatterns = [
    path('', include(router.urls)),
]
