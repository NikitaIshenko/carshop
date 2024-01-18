from django.shortcuts import render
from users.models import Client, Saller
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

def index(request):

    context = {
        "title": "Пользователи",
        "clients": Client.objects.all(),
        "sallers": Saller.objects.all()
    }
    return render(request, 'users/index.html', context)

class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'
    template_name = "main/update.html"
    extra_context = {'title': "Изменить клиента"}
    success_url = reverse_lazy('users:index')

class ClientDelete(DeleteView):
    model = Client
    template_name = "main/delete.html"
    extra_context = {'title': "Удалить клиента"}
    success_url = reverse_lazy('users:index')

class SallerUpdate(UpdateView):
    model = Saller
    fields = '__all__'
    template_name = "main/update.html"
    extra_context = {'title': "Изменить продавца"}
    success_url = reverse_lazy('users:index')

class SallerDelete(DeleteView):
    model = Saller
    template_name = "main/delete.html"
    extra_context = {'title': "Удалить продавца"}
    success_url = reverse_lazy('users:index')

class ClientCreate(CreateView):
    model = Client
    fields = "__all__"
    template_name = "main/add.html"
    extra_context = {'title': "Добавить клиента"}
    success_url = reverse_lazy('users:index')

class SallerCreate(CreateView):
    model = Saller
    fields = "__all__"
    template_name = "main/add.html"
    extra_context = {'title': "Добавить продавца"}
    success_url = reverse_lazy('users:index')
    
