from django.db import models


# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    text = models.TextField(max_length=255, null=True)


class Instruction(models.Model):
    step = models.TextField(max_length=255, blank=True)
    time = models.DurationField(blank=True, null=True)


class Hint(models.Model):
    text = models.TextField(max_length=255, null=True)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    picture = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True, related_name='recipes')
    instructions = models.ManyToManyField(Instruction, blank=True, related_name='recipes')
    hints = models.TextField(max_length=255, null=True, blank=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Shopping(models.Model):
    title = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, blank=True)

'''
class Ingredient(models.Model):
    unit = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    
class Ingredient(models.Model):
    title = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, blank=True)
'''

