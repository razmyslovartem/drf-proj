# app_users/urls.py

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from app_users.views import UserRegisterAPIView
from app_users.views import UserViewSet

from .views import CreatePaymentView
from .views import PaymentListAPIView

app_name = "app_users"
router = DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="payments-list"),
    path("payments/create/", CreatePaymentView.as_view(), name="payment-create"),
    path("users/", include(router.urls)),
    path("users/register/", UserRegisterAPIView.as_view(), name="users-register"),
]
