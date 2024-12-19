from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class PythonModule(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    published = models.BooleanField()
    display_order = models.IntegerField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    updated_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f'{self.title}'