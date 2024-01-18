from django.db import models


class Automobile(models.Model):
    engine_capacity = models.PositiveIntegerField("Обём двигателя")
    issue_year = models.PositiveIntegerField("Год выпуска")
    power = models.PositiveIntegerField("Мощность")
    win = models.CharField("Вин номер", max_length=30)
    model_auto = models.ForeignKey(
        "automobile.AutomobileModel",
        on_delete=models.CASCADE,
        related_name="automobiles",
        verbose_name="Модель автомобиля",
    )
    equipment = models.ForeignKey(
        "automobile.Equipment",
        on_delete=models.CASCADE,
        related_name="automobiles",
        verbose_name="Комплектация",
    )

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ('pk',)

    def __str__(self) -> str:
        return f"{self.model_auto} {self.issue_year}г."


class AutomobileModel(models.Model):
    name = models.CharField("Наименование модели автомобиля")
    mark_auto = models.ForeignKey(
        "automobile.AutomobileMark",
        on_delete=models.CASCADE,
        related_name="automobile_models",
        verbose_name="Марка автомобиля",
    )

    class Meta:
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модель автомобилей"

    def __str__(self) -> str:
        return f"{self.mark_auto} {self.name}"


class AutomobileMark(models.Model):
    name = models.CharField("Наименование марки автомобиля")

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марка автомобилей"

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):
    body_color = models.CharField("Цвет кузова", max_length=60)
    heated_wheel = models.BooleanField("Наличие подогрева руля")
    electric_window = models.BooleanField("Наличие электрических стеклоподъемников")
    interior_color = models.CharField("Цвет салона", max_length=60)
    interior_trim = models.CharField("Отделка салона", max_length=60)
    parking_sensor = models.BooleanField("Наличие датчика парковки")
    center_lock = models.BooleanField("Наличие центрального замка")

    class Meta:
        verbose_name = "Комплектация"
        verbose_name_plural = "Комплектации"

    def __str__(self) -> str:
        return f"Комплектация №{self.id}"

