from django.urls import path
from . import views
urlpatterns = [
    path('', views.mall),
    path('<int:id>/', views.products, name='product'),
]