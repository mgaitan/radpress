from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('radpress.urls'))
]
