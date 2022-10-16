from django.db import models

# Create your models here.
class Example(models.Model):
    name = models.CharField(max_length=35)
    ls = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name

class SubExample(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE)
    name = models.CharField(max_length = 34)
    smth = models.CharField(max_length=45)

    def __str__(self):
        return self.name