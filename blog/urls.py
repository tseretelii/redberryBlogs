from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CategoryViewSet, EmailLoginAPIView, GetBlog

urlpatterns = [
    path('blogs/', BlogViewSet.as_view(), name="instances"),
    path('blogs/<int:id>/', GetBlog.as_view(), name = 'get_blog'),
    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name = 'category'),
    path('login/', EmailLoginAPIView.as_view(), name = 'login')
]