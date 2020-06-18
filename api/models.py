from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    color_choices = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('INDEGO', 'Indigo'),
        ('VIOLET', 'Violet'),
        ('BLACK', 'Black'),
        ('WHITE', 'White')
    ]
    color_name = models.CharField(
        max_length=9,
        choices=color_choices,
        default='BLACK',
    )

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.color} {self.manufacturer} {self.shoe_type} size {self.size}'