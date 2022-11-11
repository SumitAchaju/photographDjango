from unicodedata import category
from django.db import models
from Account.models import User

class PostImage(models.Model):
    image = models.ImageField(upload_to="PostImages")

    def __str__(self):
        return self.image.name

class Comment(models.Model):
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.comment_by.username

class Category(models.Model):
    image = models.ImageField(upload_to="CategoryImage")
    discription = models.CharField(max_length=50)
    title = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    caption = models.TextField(null=True,blank=True)
    postimage = models.ManyToManyField(PostImage)
    like_by = models.ManyToManyField(User,related_name="like_users",blank=True)
    comment = models.ManyToManyField(Comment,related_name="comments",blank=True)
    post_date = models.DateTimeField(null=True,blank=True)
    category = models.ManyToManyField(Category,default=1)

    def __str__(self):
        return self.user.username
