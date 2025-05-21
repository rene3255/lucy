from django.db import models
from applications.abstracts.managers.global_abstract_manager import AbstractManager


class AbstractModel(models.Model):
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AbstractManager()

    def soft_delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} {self.id}"
