from django.test import TestCase
from .models import *
# Create your tests here.


class ImageTestClass(TestCase):
    def setUp(self):
        self.new = Post(title='new',repo_url='x.com',live_link="www.cc.com")

    def test_instances(self):
        self.assertTrue(isinstance(self.new,Post))    

    def test_save_image(self):
        self.post_test.save_post()
        after = Post.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.post_test.delete_post()
        images = Post.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.post_test.save_image()
        self.post_test.update_post(self.post_test.id, 'MEDIA/test.jpg')
        changed_img = Post.objects.filter(image='MEDIA/test.jpg')
        self.assertTrue(len(changed_img) > 0)