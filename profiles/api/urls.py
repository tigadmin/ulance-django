from django.urls import path
from . import views
from . import serializers
app_name = 'profilesapi'

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='profile-list-api'),
    path('<user__username>/update/', views.ProfileUpdateAPIView.as_view(), name='profile-create-api'),
    path('user/<user__username>/', views.ProfileDetailAPIView.as_view(), name='profile-detail-api'),
  #  path('skills/', views.SkillListAPIView.as_view(), name='skill-list-api'),
    path('skill/create/', views.SkillCreateAPIView.as_view(), name='skill-create-api'),
    path('skill/<id>/', views.SkillDetailAPIView.as_view(), name='skill-detail-api'),
  #  path('links/', views.LinkListAPIView.as_view(), name='link-list-api'),
    path('link/create/', views.LinkCreateAPIView.as_view(), name='link-create-api'),
    path('link/<pk>/', views.LinkDetailAPIView.as_view(), name='link-detail-api'),
    path('<user__username>/links/', views.UserLinkListAPIView.as_view(), name='user-link-list-api'),
   # path('<user__username/')
    path('portfolio/create/', views.PortfolioCreateAPIView.as_view(), name='portfolio-create-api'),
    path('<user__username>/portfolio', views.PortfolioDetailAPIView.as_view(), name='portfolio-detail-api'),
    path('level/create/', views.LevelCreateAPIView.as_view(), name='level-create-api'),
    path('level/<pk>/', views.LevelDetailAPIView.as_view(), name='level-detail-api'),
    path('<user__username>/levels/', views.UserLevelListAPIView.as_view(), name='user-level-list-api'),
    path('certification/<pk>/', views.CertificationDetailAPIView.as_view(), name='certification-detail-api'),
    path('certification/create/', views.CertificationCreateAPIView.as_view(), name='certification-create-api'),



]
