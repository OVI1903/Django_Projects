from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('all_members/', views.control, name='control'),
    path('all_members/details/<int:id>', views.details, name='details'),
]
