from django.conf.urls import url, include
from .api.router import rutasEjemplo
urlpatterns = [
    url('v1/', include(rutasEjemplo.urls))
]
