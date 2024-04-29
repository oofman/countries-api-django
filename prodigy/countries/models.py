from django.db import models

# Create your models here.

class Countries(models.Model):
    title = models.CharField(max_length=200)
    alpha2 = models.CharField(max_length=2,default=None)
    alpha3 = models.CharField(max_length=3,default=None)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title