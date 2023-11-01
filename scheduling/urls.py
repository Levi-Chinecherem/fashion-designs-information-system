from django.urls import path
from . import views

urlpatterns = [
    path('available_slots/', views.view_available_slots, name='view_available_slots'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('appointments/<int:appointment_id>/', views.view_appointment, name='view_appointment'),
]
