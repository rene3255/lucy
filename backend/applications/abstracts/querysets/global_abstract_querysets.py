from django.utils import timezone
from django.db import models
from datetime import timedelta


class AbstractQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)

    def recent(self, days=7):
        since = timezone.now() - timedelta(days=days)
        return self.filter(created_at__gte=since)
