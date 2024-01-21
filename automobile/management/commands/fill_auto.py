from django.core.management import BaseCommand
from automobile.models import Automobile, AutomobileMark, AutomobileModel, Equipment, Color, Body, Interior
import random
import string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--wipe",
            action="store_true",
        )

    def handle(self, *args, **options):
        if options["wipe"]:
            Automobile.objects.all().delete()
            AutomobileMark.objects.all().delete()
            AutomobileModel.objects.all().delete()
            Equipment.objects.all().delete()
            Body.objects.all().delete()
            Interior.objects.all().delete()
            Color.objects.all().delete()

        marks = [
            {"BMW": ["X1", "X2", "X3", "X6", "I8", "3 GT", "5 GT"]},
            {"Ford": ["Mustang", "Focus", "Fiesta", "Modeo", "GT", "Kuga"]},
            {"Jaguar": ["XF", "XE", "XJ", "X-TYPE", "S-TYPE", "E-PACE", "F-PACE"]},
            {"KIA": ["Optima", "RIO", "K5", "Ceed", "Cerato", "Sportage", "Stinger"]},
            {"Misubishi": ["3000 GT", "Galant", "L200", "Lancer", "Colt", "Eclipce"]},
            {"Volkswagen": ["Polo", "Passat", "Tiguan", "Taos", "Golf", "Jetta", "Touareg"]},
            {"Mercedes": ["CLS", "GL", "A-класс", "B-класс", "C-класс", "E-класс", "S-класс"]},
        ]

        print("Создаем модели машин!")

        for mark in marks:
            for k, v in mark.items():
                mark = AutomobileMark.objects.create(name=k)
                for model in v:
                    AutomobileModel.objects.create(name=model, mark_auto=mark)

        colors = ["Черный", "Белый", "Розовый", "Красный", "Синий", "Желтый"]

        for color in colors:
            Color.objects.create(title=color)
        
        colors = Color.objects.all()

        interior_trims = ["Алькантара", "Кожа", "Ткань"]
        body_types = ["Седан", "Лифтбек", "Хэтчбэк", "Джип"]

        for i in range(10):
            Interior.objects.create(color=random.choice(colors), decoration=random.choice(interior_trims))
            Body.objects.create(color=random.choice(colors), type_body=random.choice(body_types))


        
        bodies = Body.objects.all()
        interiors = Interior.objects.all()
        bools = [True, False] 

        print("Создаем комплектации для машин!")

        for _ in range(30):
            Equipment.objects.create(
                body = random.choice(bodies),
                interior = random.choice(interiors),
                heated_wheel = random.choice(bools),
                electric_window = random.choice(bools),
                parking_sensor = random.choice(bools),
                center_lock = random.choice(bools)
            )

        for i in range(50):
            Automobile.objects.create(
                engine_capacity = random.randint(1, 8),
                issue_year = random.randint(1990, 2023),
                power = random.randint(150, 300),
                win = "".join(random.choices(string.ascii_uppercase + string.digits, k=17)),
                model_auto = AutomobileModel.objects.all().order_by("?").first(),
                equipment = Equipment.objects.all().order_by("?").first(),
            )
            print(f"{i+1} машина создана!")
