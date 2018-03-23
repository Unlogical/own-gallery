from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views import generic
from .models import Image


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


from .forms import ImageForm

@login_required
def post_image(request):
    user = request.user
    images = Image.objects.filter(user = user)
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = user
            image.save()
    else:
        form = ImageForm()

    return render(request, 'home.html', {'images':images, 'form':form},)