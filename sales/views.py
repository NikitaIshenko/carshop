from django.shortcuts import render
from sales.models import Sale
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

def index(request):

    context = {
        'title': "Подажи",
        'sales': Sale.objects.all()

    }

    return render(request, 'sales/index.html', context)

class SaleUpdate(UpdateView):
    model = Sale
    fields = '__all__'
    template_name = "main/update.html"
    extra_context = {'title': "Изменить продажу"}
    success_url = reverse_lazy('sales:index')

class SaleDelete(DeleteView):
    model = Sale
    template_name = "main/delete.html"
    extra_context = {'title': "Удалить продажу"}
    success_url = reverse_lazy('sales:index')

class SaleCreate(CreateView):
    model = Sale
    fields = "__all__"
    template_name = "main/add.html"
    extra_context = {'title': "Добавить продажу"}
    success_url = reverse_lazy('sales:index')
