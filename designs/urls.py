# designs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_design, name='upload_design'),
    path('list/', views.design_list, name='design_list'),
    path('manage-client-info/', views.manage_client_info, name='manage_client_info'),
    path('design/<int:design_id>/', views.design_detail, name='design_detail'),
    path('design/<int:design_id>/update/', views.update_design, name='update_design'),
    path('design/<int:design_id>/delete/', views.delete_design, name='delete_design'),
]
