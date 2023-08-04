from django.urls import path
from . import views 


urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('resumes/', views.ResumeListView.as_view(), name='resume-list'),
    path('adverts/', views.AdvertListView.as_view(), name='advert-list'),
    path('applications/', views.ApplicationListView.as_view(), name='application-list'),
    path('company/', views.CompanyListView.as_view(), name='company-list'),
    #path('ilan_öneri/<int:userid>/', views.recommended_jobs, name='recommended_jobs'),
    path('öneri/<int:userid>/', views.get_relevant_applications, name='get_relevant_applications'),
    path('test', views.test, name='test'),
]