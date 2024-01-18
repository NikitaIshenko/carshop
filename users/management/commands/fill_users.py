from django.core.management import BaseCommand
from users.models import Client, Saller
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
            Client.objects.all().delete()
            Saller.objects.all().delete()

        second_names = ["Александрович", "Викторович", "Владимирович", "Палов", "Константинович"]

        for i in range(25):
            
            full_name = f"{fake.last_name_male()} {fake.first_name_male()} {random.choice(second_names)}"
            Client.objects.create(
                full_name=full_name,
                address=fake.address(),
                dob=datetime.date.today() - datetime.timedelta(random.randint(20, 35) * 365),
                phone_number=fake.phone_number(),
            )

            full_name = f"{fake.last_name_male()} {fake.first_name_male()} {random.choice(second_names)}"

            Saller.objects.create(
                full_name=full_name,
                phone_number=fake.phone_number(),
                email=fake.email()
            )
            print(f"{i+1} Продавец и клиент создан")