from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('home/', views.post_image, name='post_image'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'delete/(?P<pk>\d+)/', views.delete_image, name='delete_image')
]