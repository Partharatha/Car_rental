from django.urls import path
from rentalcars import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'rentalcars'

urlpatterns = [
    path('', views.rental_cars_list, name='rental_cars_list'),
    path('car/<int:pk>/', views.car_detail, name='car'),
    path("details/<int:pk>/", views.details, name="details_rent"),
    path("final/<int:pk>/", views.final, name="finalprice"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

