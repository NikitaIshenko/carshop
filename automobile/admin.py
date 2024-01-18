from django.contrib import admin
from automobile.models import Automobile, AutomobileMark, AutomobileModel

automobile_models = [Automobile, AutomobileMark, AutomobileModel]

for model in automobile_models:
    admin.site.register(model)
