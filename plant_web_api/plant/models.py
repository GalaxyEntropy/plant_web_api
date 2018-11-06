from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "t_user"
        unique_together = (("name"),)

