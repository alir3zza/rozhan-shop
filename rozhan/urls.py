
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("product/", include("product.urls")),
    path("contact/", include("contact.urls")),
    path("account/", include("account.urls")),
    path("cart/", include("cart.urls")),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

