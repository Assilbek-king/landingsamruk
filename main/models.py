from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'

class Tovar(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    status = models.IntegerField(default=0, blank=True)


    def __str__(self):
        return f'{self.title}'

class Photo(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f'{self.logo}'


class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    comment = models.TextField(blank=True,null=True)
    categoriya = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'


