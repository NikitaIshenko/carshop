from django.contrib import admin
from automobile.models import Automobile, AutomobileMark, AutomobileModel, Color, Body, Interior

automobile_models = [Automobile, AutomobileMark, AutomobileModel, Color, Body, Interior]

for model in automobile_models:
    admin.site.register(model)
