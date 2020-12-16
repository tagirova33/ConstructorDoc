from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name = 'Имя')
    last_name = models.CharField(max_length=30, verbose_name = 'Фамилия')
    fam_name = models.CharField(max_length=30, verbose_name = 'Отчество')
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' +self.fam_name
