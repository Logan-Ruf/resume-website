from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.MyView.as_view(), name='my-view')
]