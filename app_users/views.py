# app_users/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import Payment
from .serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    # какие фильтры включаем
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # фильтрация по полям (курс, урок, способ оплаты)
    filterset_fields = ["paid_course", "paid_lesson", "payment_method"]

    # поиск по email пользователя
    search_fields = ["user__email"]

    # сортировка по дате и сумме
    ordering_fields = ["payment_date", "amount"]
    ordering = ["-payment_date"]  # дефолт — новые сверху
