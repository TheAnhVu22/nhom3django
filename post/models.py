from django.db import models

# Create your models here.
class cate_post(models.Model):
    cate_post_name = models.CharField(max_length=255)
    cate_post_slug = models.SlugField(max_length=255, default=None)
    def __str__(self):
        return self.cate_post_name 

class post(models.Model):
    post_name = models.CharField(max_length=255)
    post_content= models.TextField(max_length=255)
    post_image = models.ImageField(upload_to="images", null=False, default=None)
    post_author = models.CharField(max_length=255)
    post_slug = models.SlugField(max_length=255, default=None)
    cate_post_id = models.ForeignKey(cate_post,related_name='posts', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.post_name},{self.post_content},{self.post_image},{self.post_author}" 