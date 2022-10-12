from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.forms import RegisterChefForm, RegisterClientForm
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class RegisterChef(View):
    def get(self, request):
        form = RegisterChefForm()
        context = {"form": form}
        return render(request, "registration/register_chef.html", context)
    def post(self, request):
        form = RegisterChefForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/register_chef.html", context)

class RegisterClient(View):
    def get(self, request):
        form = RegisterClientForm()
        context = {"form": form}
        return render(request, "registration/register_client.html", context)
    def post(self, request):
        form = RegisterClientForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/register_client.html", context)

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = 'profile.html'
