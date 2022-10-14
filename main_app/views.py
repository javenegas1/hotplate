from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.forms import RegisterChefForm, RegisterClientForm
from main_app.models import Chef, Request
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

class ChefsList(TemplateView):
    template_name = 'chefs_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = self.request.GET.get('')

        if location != None:
            context["chefs"] = Chef.objects.filter(location__icontains=location)
            context["header"] = "Searching for chefs around {}".format(location)
        else:
            context["chefs"] = Chef.objects.filter()
            context["header"] = "Chefs around here"
        return context

class ChefDetail(DetailView):
    model = Chef
    template_name = "chef_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chefs'] = Chef.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class RequestCreate(CreateView):

    def post(self, request, pk):
        title = request.POST.get("title")
        summary = request.POST.get("summary")
        people = request.POST.get("people")
        date_of_event = request.POST.get("date_of_event")
        chef = Chef.objects.get(pk=pk)
        Request.objects.create(title=title, summary=summary, people=people, date_of_event=date_of_event, chef=chef, user=self.request.user)
        return redirect('chef_detail', pk=pk)

@method_decorator(login_required, name='dispatch')
class RequestUpdate(UpdateView):
    model = Request 
    fields = ['title', 'summary', 'people', 'date_of_event']
    template_name = "request_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Request.objects.all()
        return context

    def get_success_url(self):
        return '/chefs/{}'.format(self.object.chef_id)

class RequestDelete(DeleteView):
    model = Request
    template_name = "request_delete_confirm.html"
    # success_url = "/chefs/{}".format()

    def get_success_url(self):
        return '/chefs/{}'.format(self.object.chef_id)