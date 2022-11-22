from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Profile(models.Model):
    """model for user's profile """
    user = models.ForeignKey(user, on_delete=models.CASCADE, )
    position = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_created=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.user}'
