from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

#   path('home/', views.post_image(name='home.html')),
    path('home/', views.post_image, name='post_image'),

    path('signup/', views.SignUp.as_view(), name='signup'),
]