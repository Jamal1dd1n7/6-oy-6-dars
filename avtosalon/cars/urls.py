from django.urls import path
from .views import home, brend, car_detail

urlpatterns = [
    path('', home, name='home'),
    path('brend/<int:brend_id>/', brend, name='brends'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
]