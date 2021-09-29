from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index')

]

#we are adding django site admin urls
urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls'))
]
