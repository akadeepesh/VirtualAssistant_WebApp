from django.db import models

class Member(models.Model):
    Receivers_name = models.CharField(max_length=30, null=True)
    Receivers_phone_no = models.IntegerField(null=True)
    Insta_username = models.CharField(max_length=30, null=True)
    Insta_password = models.CharField(max_length=30, null=True)
    Insta_receiver = models.CharField(max_length=30, null=True)
    def __str__(self):
        return f"{self.Receivers_name} {self.Receivers_phone_no}"
# Create your models here.
