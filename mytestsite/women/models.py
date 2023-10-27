from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.contrib import admin

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=300, unique=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Вміст')
    photo = models.ImageField(upload_to='photos/%Y/%d/%m/', verbose_name='Фотографії')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публікації')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорії')
    @admin.display(boolean=True)
    def check_len(self):
        return len(self.title) > 8
    def __str__(self):
        return self.title
    def generate_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})
    class Meta:
        verbose_name = 'Відомі жінки'
        verbose_name_plural = verbose_name
        ordering = ('cat',)

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True, verbose_name='URL')
    def __str__(self):
        return self.name
    def generate_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name_plural = "Категорії"
        verbose_name = verbose_name_plural

class Test_table(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    phone_num = PhoneNumberField(blank=False, unique=True)
    email_adres = models.EmailField(unique=True, blank=False)
    def __str__(self):
        return self.name
    def generate_url(self):
        return reverse('test', kwargs={'name': self.name, 'age': self.age})
    class Meta:
        verbose_name_plural = 'Тестова таблиця'
        verbose_name = verbose_name_plural
        ordering = ('id',)
class User_information(models.Model):
    user_name = models.CharField(max_length=250)
    user_surname = models.CharField(max_length=250)
    marks = models.IntegerField()
    request_date = models.DateField(auto_now_add=True)
