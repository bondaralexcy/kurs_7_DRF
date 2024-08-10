from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    FREQUENCY_UNITS = [
        ("minutes", "минуты"),
        ("hours", "часы"),
        ("days", "дни"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец привычки",
        **NULLABLE,
    )
    place = models.CharField(max_length=200, verbose_name="Место привычки")
    time = models.DateTimeField(verbose_name="Дата и время привычки")
    action = models.CharField(max_length=200, verbose_name="Действие")
    is_pleasant = models.BooleanField(verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    frequency_number = models.PositiveIntegerField(verbose_name="Как часто")
    frequency_unit = models.CharField(
        max_length=10,
        choices=FREQUENCY_UNITS,
        default="days",
        verbose_name="Интервалы времени",
    )
    reward = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.DurationField(verbose_name="Время выполнения")
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"{self.user} - {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
