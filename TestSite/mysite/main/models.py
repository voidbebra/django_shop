from django.db import models
from django_resized import ResizedImageField

class Prod(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    img = ResizedImageField(size=[600, 400],crop=['top','left'],upload_to='main/media/pictures', null=True, blank=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'is_sale': self.is_sale,
            'sale_price': self.sale_price,
            'description': self.description,
            'img': self.img
            # Добавьте другие поля, которые вам нужны
        }