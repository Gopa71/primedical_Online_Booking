from django.db import models
from django.urls import reverse
# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    banner=models.ImageField(upload_to='bnr')
    photo=models.ImageField(upload_to='pic')
    available=models.BooleanField(default=True)
    desc=models.TextField(blank=True)
    title_1=models.TextField(max_length=250)
    title_2=models.TextField(max_length=250)
    title_3=models.TextField(max_length=250)
    title_4=models.TextField(max_length=250)
    desc_1=models.TextField(blank=True)
    desc_2=models.TextField(blank=True)
    desc_3=models.TextField(blank=True)
    desc_4=models.TextField(blank=True)

    def __str__(self):      
        return '{}'.format(self.name)

class Service(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    banner=models.ImageField(upload_to='br')
    desc=models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='Service'
        verbose_name_plural='Services'

    def __str__(self):      
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('shop:products_by_category',args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    banner=models.ImageField(upload_to='bar')
    desc=models.TextField(blank=True)
    photo=models.ImageField(upload_to='pic')
    available=models.BooleanField(default=True)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    desc=models.TextField(blank=True)
    title_1=models.TextField(max_length=250)
    title_2=models.TextField(max_length=250)
    title_3=models.TextField(max_length=250)
    title_4=models.TextField(max_length=250)
    desc_1=models.TextField(blank=True)
    desc_2=models.TextField(blank=True)
    desc_3=models.TextField(blank=True)
    desc_4=models.TextField(blank=True)

    class Meta:
        
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        
        return '{}'.format(self.name)