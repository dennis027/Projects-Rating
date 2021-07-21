from django.test import TestCase
from .models import *
# Create your tests here.


class PostTestClass(TestCase):
    def setUp(self):
        self.new = Post(title='new',repo_url='x.com',live_link="www.cc.com")

    def test_instances(self):
        self.assertTrue(isinstance(self.new,Post))    

    def test_save_post(self):
        self.post_test.save_post()
        after = Post.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_post(self):
        self.post_test.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

    def test_update_post(self):
        self.post_test.save_post()
        self.post_test.update_post(self.post_test.id, 'MEDIA/test.jpg')
        changed_img = Post.objects.filter(post='MEDIA/test.jpg')
        self.assertTrue(len(changed_img) > 0)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.new = Profile(user="kimani",profile_picture="a.jpg",bio="hello")

    def test_instances(self):
        self.assertTrue(isinstance(self.new,Profile))    

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_post(self):
        self.profile_test.save_post()
        self.profile_test.update_profile(self.profile_test.id, 'MEDIA/test.jpg')
        changed_img = Profile.objects.filter(profile='MEDIA/test.jpg')
        self.assertTrue(len(changed_img) > 0)        