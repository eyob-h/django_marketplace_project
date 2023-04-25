from django.contrib import admin
from django.urls import path, include
# from core.views import index
# from core.views import contact
# from django.urls import include

#Shouldn't be done in production!
from django.conf import settings
from django.conf.urls.static import static
#Shouldn't be done in production!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path("", include('core.urls')),
    path('dashboard/',include('dashboard.urls')),
    # path("contact/", contact, name="contact")
    # path('puddle/', include('idx')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
