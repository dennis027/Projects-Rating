from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.class Post(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)  
    author= models.ForeignKey(User,on_delete = models.CASCADE)  
    image= models.ImageField(upload_to='MEDIA/')
    votes_total = models.IntegerField(default=1)

    def publication_date(self):
        return self.pub_date.strftime('%b %e, %Y')
