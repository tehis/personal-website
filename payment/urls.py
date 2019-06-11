from django.urls import path

from .  import  views


app_name = 'payment'

urlpatterns = [
    path('', views.PaymentView.as_view(), name='index'),
    path('free_pdf', views.GenerateFreePdf.as_view(), name='free_pdf'),
    path('callback/', views.PaymentCallbackView.as_view(), name='payment_callback'),
]