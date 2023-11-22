from django.db import models

class DarkUser(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.last_name

class Post(models.Model):
    owner = models.ForeignKey(DarkUser, null=True, on_delete=models.CASCADE)
    text = models.CharField()
