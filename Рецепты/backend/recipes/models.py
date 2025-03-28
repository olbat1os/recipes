from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text='Время приготовления в минутах')
    servings = models.IntegerField(help_text='Количество порций')
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
