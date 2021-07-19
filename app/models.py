from django.db import models
from django.contrib.auth.models import User

# Category モデルを作成
class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
       return self.title

class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.title