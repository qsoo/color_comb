from django.db import models
#user
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_colors')
    title = models.CharField(max_length=100)
    content = models.TextField()
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    color3 = models.CharField(max_length=50)
    color4 = models.CharField(max_length=50)
    color5 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

