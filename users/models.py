from django.db import models


class Client(models.Model):
    full_name = models.CharField("Полное имя", max_length=155)
    address = models.TextField("Адресс")
    dob = models.DateField("Дата рождения")
    phone_number = models.CharField("Номер телефона", max_length=30)
    registration_date = models.DateTimeField("Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self) -> str:
        return self.full_name


class Saller(models.Model):
    full_name = models.CharField("Полное имя", max_length=155)
    phone_number = models.CharField("Номер телефона", max_length=30)
    email = models.EmailField("Email")

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self) -> str:
        return self.full_name
