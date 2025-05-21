from django.db import models
from applications.abstracts.querysets.global_abstract_querysets import AbstractQuerySet


class AbstractManager(models.Manager):
    def get_queryset(self):
        return AbstractQuerySet(self.model, using=self._db).active()

    def actives_and_inactives(self):
        return AbstractQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset()

    def inactive(self):
        return self.actives_and_inactives().inactive()

    def recent(self, days=7):
        return self.get_queryset().recent(days=days)
