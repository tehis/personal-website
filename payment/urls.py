from django.urls import path

from .  import  views


urlpatterns = [
    path('', views.PaymentView.as_view(), name='payment'),
    path('callback/', views.PaymentCallbackView.as_view(), name='payment_callback'),
]