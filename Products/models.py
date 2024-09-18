from django.db import models
from django.urls import reverse


class Product(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name= "Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name = models.CharField(max_length=30, blank=False, verbose_name = "Назва товару")
    describe = models.CharField(max_length=2000, blank=True, verbose_name = "Характеристики")
    price = models.FloatField(blank=False, verbose_name = "Ціна")
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = "Категорії")
    
    # def __repr__(self):
    #     return 'Image(%s, %s)' % (self.title, self.image)
    def __str__(self) -> str:
        return f"{self.name}\t{self.describe}\t------\t{self.price} грн"
    

    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = " Продукт "
        verbose_name_plural = " Продукти "
        ordering = [ 'name']
        
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name = "Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = " Категорія "
        verbose_name_plural = " Категорії "
        ordering = [ 'name']