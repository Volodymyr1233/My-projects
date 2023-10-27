from django.contrib import admin
from .models import Women, Category, Test_table
import random
# Register your models here.

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    verbose_name = 'Жінки світу'
    list_display = ('id', 'title', 'slug', 'photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title', 'photo')
    list_editable = ('is_published','cat')
    list_filter = ('title', 'time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('id',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Категорії'
    list_display = ('id', 'name', 'slug')
    list_filter = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    ordering = ('id',)
@admin.register(Test_table)
class Test_tableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'phone_num', 'email_adres')
    list_filter = ('name',)
    ordering = ('id',)
    fields = (('name', 'surname'), 'age', ('phone_num', 'email_adres'))