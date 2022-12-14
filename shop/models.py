import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


def upload_to(instance, filename: str) -> str:
    return os.path.join("static", "products", instance.title, filename)


class Product(models.Model):
    choices = (
        ("available", "В наличии"),
        ("oreder", "Под заказ"),
        ("waiting", "Ожидается поступление"),
        ("not_availabel", "Нет в наличии"),
        ("not_produced", "Не производится"),
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["title"]

    title = models.CharField(_("title"), max_length=255)
    barcode = models.CharField("Артикул", max_length=100)
    price = models.DecimalField("Цена", decimal_places=2, max_digits=10)
    status = models.CharField("Статус", choices=choices, max_length=100)
    image = models.ImageField("Фото", upload_to=upload_to)

    def __str__(self):
        return self.title

    @staticmethod
    def change_file_format(image: os.PathLike):
        path_to_img = os.path.dirname(image)
        filename = os.path.basename(image)
        with Image.open(image) as image:
            path_to_save = os.path.join(path_to_img, f"{filename.split('.')[0]}.webp")
            image.save(path_to_save)

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.change_file_format(self.image.path)
