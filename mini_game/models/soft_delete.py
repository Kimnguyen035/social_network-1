from django.db import models
from django.utils import timezone

class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(default=None)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True