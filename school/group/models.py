from django.db import models


class Group(models.Model):
    id = models.BigAutoField
    group_name = models.CharField(max_length=64)
    number_of_group_members = models.PositiveSmallIntegerField()
    group_type = models.CharField(max_length=64)

    def get_full_info(self):
        return f'{self.id} - {self.group_name} - {self.number_of_group_members} - {self.group_type}'
