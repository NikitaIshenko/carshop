from django.shortcuts import render
from automobile.models import Automobile
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

def index(request):
    automobiles = Automobile.objects.all()
    context = {
        "automobiles": automobiles,
        "title": "Автомобили"
    }
    return render(request, 'automobile/index.html', context)

class AutomobileUpdate(UpdateView):
    model = Automobile
    fields = '__all__'
    template_name = "main/update.html"
    extra_context = {'title': "Изменить автомобиль"}
    success_url = reverse_lazy('automobile:index')

class AutomobileDelete(DeleteView):
    model = Automobile
    template_name = "main/delete.html"
    extra_context = {'title': "Удалить автомобиль"}
    success_url = reverse_lazy('automobile:index')

class AutomobileCreate(CreateView):
    model = Automobile
    fields = "__all__"
    template_name = "main/add.html"
    extra_context = {'title': "Добавить автомобиль"}
    success_url = reverse_lazy('automobile:index')

