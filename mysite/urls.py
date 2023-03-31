from django.urls import path
from django.urls import include
from django.contrib import admin

from docs.yasg.urls import urlpatterns as yasg_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("payments/", include("payme.urls")),
    path("shop/", include("shop.urls"))
]

urlpatterns += yasg_urls
