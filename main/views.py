from django.shortcuts import render, redirect
from automobile.models import Automobile, Equipment, AutomobileMark
from users.models import Saller, Client
from sales.models import Sale
from django.db.models import Sum
from django.db.models import Count

def main(request):
    return redirect("automobile:index")

def mark(request):
    automobiles = Automobile.objects.all()
    context = {
        'title': "Наличие комплектаций",
        'automobiles': automobiles
    }
    return render(request, 'main/mark.html', context)

def top_saller(request):
    sales_sum_by_seller = Sale.objects.values('saller').annotate(total_sales=Sum('sum'))
    seller_with_max_sales = sales_sum_by_seller.order_by('-total_sales').first()
    saller = Saller.objects.get(id=seller_with_max_sales['saller'])
    context = {
        'title': "Продавец с наибольшем кол-вом продаж",
        "saller": saller,
        "top_saller": seller_with_max_sales
    }
    return render(request, 'main/top-saller.html', context)

def client_card(request):
    client = Client.objects.first()
    context = {
        'client': client,
        'title': "Личная карточка клиента"
    }
    return render(request, 'main/client-card.html', context)

def most_mark_eq(request):
    eq_count = Sale.objects.values('auto__equipment').annotate(equipment_count=Count('auto__equipment'))
    mark_count = Sale.objects.values('auto__model_auto__mark_auto').annotate(mark_count=Count('auto__model_auto__mark_auto'))
    most_eq_name = eq_count.order_by('-equipment_count')[0:3]
    most_mark = mark_count.order_by('-mark_count')[0:3]
    eq_id = [i['auto__equipment'] for i in most_eq_name]
    mark_id = [i['auto__model_auto__mark_auto'] for i in most_mark]
    equipments = Equipment.objects.filter(pk__in=eq_id)
    marks = AutomobileMark.objects.filter(pk__in=mark_id)
    context = {
        'title': "Самые актуальные",
        'equipments': equipments,
        'marks': marks
    }
    return render(request, 'main/most-mark-eq.html', context)
