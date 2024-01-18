from django.db import models


class PayType(models.Model):
    name = models.CharField("Наименования способа оплаты", max_length=60)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"


class DeliveryType(models.Model):
    name = models.CharField("Наименования способа оплаты", max_length=60)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Способ доставки"
        verbose_name_plural = "Способы доставки"


class Sale(models.Model):
    date = models.DateField("Дата продажи")
    sum = models.IntegerField("Сумма продажи")
    auto = models.ForeignKey(
        "automobile.Automobile", on_delete=models.CASCADE, related_name="sales"
    )
    client = models.ForeignKey(
        "users.Client", on_delete=models.CASCADE, related_name="sales"
    )
    saller = models.ForeignKey(
        "users.Saller", on_delete=models.CASCADE, related_name="sales"
    )
    pay_type = models.ForeignKey(
        PayType, on_delete=models.CASCADE, related_name="sales"
    )
    delivery_type = models.ForeignKey(
        DeliveryType, on_delete=models.CASCADE, related_name="sales"
    )

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self) -> str:
        return f"{self.date} - {self.sum}"
