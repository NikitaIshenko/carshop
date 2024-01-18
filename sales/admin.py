from django.contrib import admin
from sales.models import PayType, DeliveryType, Sale

sales_models = [PayType, DeliveryType, Sale]

for model in sales_models:
    admin.site.register(model)
