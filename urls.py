from django.urls import path
import AppFollowUp.views as views

urlpatterns = [
	path('', views.index,name = 'index'),
	path('refresh/',views.refresh,name = 'refresh')
]