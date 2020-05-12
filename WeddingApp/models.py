from django.db import models

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

