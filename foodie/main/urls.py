from django.urls import path
from . import views

urlpatterns = [
    path('', views.login ),
    path('home', views.home ),
    path('plp', views.plp ),
    path('contact', views.contact ),
    path('product/<int:id>/', views.product ),
    path('register', views.reg),
    path('logger', views.logger),
    path('feedback', views.feedback),
]