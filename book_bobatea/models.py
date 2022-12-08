from django.db import models
from django.utils.text import slugify

# Create your models here.


class TeaMenu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.IntegerField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(TeaMenu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tea Menu'
        verbose_name_plural = 'Tea Menu'
