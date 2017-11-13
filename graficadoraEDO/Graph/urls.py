from django.conf.urls import url, include
from . import views as vi

vista = vi.views()

urlpatterns = [
    url(r'^$', vista.home),
]