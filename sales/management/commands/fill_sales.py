from django.core.management import BaseCommand
from users.models import Client, Saller
from automobile.models import Automobile
from sales.models import Sale, PayType, DeliveryType
import random
import string
from faker import Faker
import datetime

fake = Faker("ru_RU")
Faker.seed(0)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--wipe",
            action="store_true",
        )

    def handle(self, *args, **options):
        if options["wipe"]:
            Sale.objects.all().delete()
            PayType.objects.all().delete()
            DeliveryType.objects.all().delete()

        delivery = ["Доставка", "Самовызов"]
        pay = ["Безнал", "Наличные", "Кредит"]

        for d in delivery:
            DeliveryType.objects.create(name=d)

        for p in pay:
            PayType.objects.create(name=p)

        for i in range(30):
            Sale.objects.create(
                date=datetime.date.today()
                - datetime.timedelta(random.randint(180, 900)),
                sum=random.randint(1000000, 10000000),
                auto=Automobile.objects.all().order_by("?").first(),
                client=Client.objects.all().order_by("?").first(),
                saller=Saller.objects.all().order_by("?").first(),
                pay_type=PayType.objects.all().order_by("?").first(),
                delivery_type=DeliveryType.objects.all().order_by("?").first(),
            )
            print(f"{i+1} Продажа создана")
