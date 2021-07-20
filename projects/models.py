from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.class Post(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    live = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)  
    author= models.ForeignKey(User,on_delete = models.CASCADE)  
    image= models.ImageField(upload_to='MEDIA/')
    votes_total = models.IntegerField(default=1)

    def publication_date(self):
        return self.pub_date.strftime('%b %e, %Y')

    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post
class RateModel(models.Model):
    pass
    # TEN_REVIEWS= (
    #     ('10', '10','10'),
    #     ('9', '9','9'),
    #     ('8', '8','8'),
    #     ('7', '7','7'),
    #     ('6', '6','6'),
    #     ('5', '5','5'),
    #     ('4', '4','4'),
    #     ('3', '3','3'),
    #     ('2', '2','2'),
    #     ('1', '1','1'),
    # )

    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    # posts = models.ForeignKey(Post,on_delete = models.CASCADE)
    # design = models.PositiveIntegerField(choices=TEN_REVIEWS,default=0)
    # usability = models.PositiveIntegerField(choices=TEN_REVIEWS,default=0)
    # content =models.PositiveIntegerField(choices=TEN_REVIEWS,default=0)

    # class Meta:
    #     verbose_name_plural= 'Ratings'

    # def __str__(self):
    #     return self.str(self.post)   