from django.db import models


class FreeItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price=0.00)
