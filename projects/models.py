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
        posts = cls.objects.filter(title__icontains=search_term)
        return posts
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'