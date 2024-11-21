from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('view-profile/', views.view_profile, name='view-profile'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
]
