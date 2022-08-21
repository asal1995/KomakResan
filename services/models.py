from django.db import models

from services.enumoration import StateChoice


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Request(models.Model):
    service = models.ForeignKey('services.Service', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=10, choices=StateChoice.choices())
    extra_user_des = models.TextField()
    extra_staff_des = models.TextField()
    photo = models.ImageField(upload_to="images", null=True)
    created_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField(auto_now=True)


