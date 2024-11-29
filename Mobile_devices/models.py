from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.FloatField(verbose_name='Укажите цену')
    release_date = models.DateField(verbose_name='Укажите дату выпуска')
    image = models.ImageField(upload_to='device_images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    features = models.ManyToManyField('Feature', related_name='devices')

    def str(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name