from django.urls import path
from .views import vendorList, vendorDetail, hiring_ticketList, hiring_ticketDetail

urlpatterns = [
    path('<int:pk>/', vendorDetail.as_view()),
    path('', vendorList.as_view()),
    path('<int:pk>/', hiring_ticketDetail.as_view()),
    path('hiring_ticket', hiring_ticketList.as_view()),
]