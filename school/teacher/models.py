from django.db import models

class Teacher(models.Model):
    id = models.BigAutoField
    firts_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.SmallIntegerField(max_length=64)

    def __str__(self):
        return f'{self.id} - {self.firts_name} - {self.last_name} - {self.age}'
