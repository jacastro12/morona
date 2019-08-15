from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login
from django.contrib.auth import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('appmacas.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
