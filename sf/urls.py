from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from main.forms import PetalForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/', RegistrationView.as_view(form_class=PetalForm)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
