from django.urls import path

from apps.shop.views import GeneratePayLinkAPIView


urlpatterns = [
    path('pay-link/', GeneratePayLinkAPIView.as_view(), name='generate-pay-link')
]
