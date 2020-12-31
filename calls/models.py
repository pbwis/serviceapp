from django.db import models
import uuid


class Call(models.Model):
    printer = models.CharField(max_length=100, null=True, blank=True)
    page_count_b = models.IntegerField(default=0)
    page_count_c = models.IntegerField(default=0)
    action = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for call')

    def __str__(self):
        return str(self.printer)