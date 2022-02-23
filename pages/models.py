from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    img_url = models.URLField()
    img_alt = models.CharField(max_length=120)
    external_url = models.URLField()
    external_text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
