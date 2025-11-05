from django.urls import path
from carsapp import views

urlpatterns=[
    path('',views.Companylist,name='companies'),
    path('<int:id>',views.Company_details,name='details'),
    path('calcemi/<int:id>',views.calcemi,name='calcemi'),
    path('product/<int:id>',views.product,name='product'),
    path('finalprice/<int:id>', views.finalprice, name='finalprice'),
    path('Bookdrive/<int:id>/',views.Bookdrive,name='Bookdrive'),
    path('enquiry/<int:id>/',views.enquiry_view,name='enquiry')
]