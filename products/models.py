from django.db import models
from users.models import CustomUser
from django.conf import settings
# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    photo = models.ImageField(null=True, upload_to='images/')
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]