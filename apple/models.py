from django.db import models


class Photo(models.Model):
    title = models.TextField(default='untitled')
    photo = models.ImageField(upload_to='%y%m%d')
    author = models.TextField(default='anonymous')
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

