from django.db import models
from django.contrib.auth.models import User

class Hurimiin_Yslol_Uilchilgee(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Tureesiin_Uilchilgee(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Neriin_Buteegdehuun(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Surgalt(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    picture = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Cart(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    yslol = models.ManyToManyField(Hurimiin_Yslol_Uilchilgee, related_name='+')
    turees = models.ManyToManyField(Tureesiin_Uilchilgee, related_name='+')
    neriin  = models.ManyToManyField(Neriin_Buteegdehuun, related_name='+')
    surgalt = models.ManyToManyField(Surgalt, related_name='+')
    hamtragch = models.ManyToManyField(Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee, related_name='+')


    def __str__(self):
        return self.userId.first_name

