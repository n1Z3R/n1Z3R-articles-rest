from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email').blank = False
User._meta.get_field('email')._unique = True


class ArticlesModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myarticles")

    def __str__(self):
        return self.name


class ArticlesLikesModel(models.Model):
    article = models.ForeignKey(ArticlesModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} like {self.article.name}"


class ArticlesCommentsModel(models.Model):
    article = models.ForeignKey(ArticlesModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=600)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment {self.article.name}"
