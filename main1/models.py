from django.db import models

class Type(models.Model):
    slug = models.SlugField(max_length=12)
    version = models.CharField(max_length=55, unique=True)
    def __str__(self):
        return f'{self.version}'

class Game(models.Model):
    CHOICES = (
        ('торг уместен', 'в наличии'),
        ('out of stock', 'нет в наличии')
    )
    name = models.CharField(max_length=55)
    date_of_issue = models.DateField()
    description = models.TextField()
    status = models.CharField(choices=CHOICES, max_length=20)
    image = models.ImageField(blank=True, upload_to='games')
    type = models.ManyToManyField(Type)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

