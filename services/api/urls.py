__author__ = '13477'
from django.urls import path
from . import views

app_name = 'servicesapi'

urlpatterns = [
    path('', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('category/create/', views.CategoryCreateAPIView.as_view(), name='category-create-api'),
    path('category/<pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create-api'),
    path('<pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),
    path('<pk>/reviews/', views.ServiceReviewListAPIView.as_view(), name='service-reviews-list-api'),
    path('review/create/', views.CreateReviewAPIView.as_view(), name='review-create-api'),
    path('review/<pk>/', views.ReviewDetailAPIView.as_view(), name='review-detail-api'),



]